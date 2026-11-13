"""LexStudy Ghana v0.3 — accounts, verified briefs, quizzes, IRAC,
flashcards and timed mocks.

Accounts are for bookmarks and progress only. All content is
currently free to browse; paid-content restrictions are NOT yet
enforced, and no payment provider is connected. Passwords are hashed
with Werkzeug and never stored in plain text. Storage is PostgreSQL
when DATABASE_URL is set (Render) and local SQLite otherwise
(see db.py); the SQLite file must not be committed.
"""

import os
from datetime import date, timedelta
from functools import wraps

from flask import (
    Flask, abort, flash, g, redirect, render_template, request,
    session, url_for,
)
from werkzeug.security import check_password_hash, generate_password_hash

from data import CASES, PLANS, SUBJECTS, get_case, get_subject, search as search_data
from db import connect, init_db
from flashcards import FLASHCARD_DECKS, all_cards, get_deck
from irac_data import SCENARIOS, get_scenario
from mocks import TIME_LIMIT_MINUTES, all_mocks, get_mock
from quizzes import QUIZZES, get_quiz
from verified_cases import VERIFIED_CASES, get_verified_case

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-change-me-in-production")
init_db()


def current_user():
    user_id = session.get("user_id")
    if not user_id:
        return None
    conn = connect()
    try:
        row = conn.execute("SELECT id, email, name FROM users WHERE id = ?", (user_id,)).fetchone()
        return dict(row) if row else None
    finally:
        conn.close()


@app.context_processor
def inject_user():
    return {"current_user": current_user()}


def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if not current_user():
            flash("Please log in to use that feature.")
            return redirect(url_for("login"))
        return view(*args, **kwargs)
    return wrapped


def all_cases():
    return VERIFIED_CASES + CASES


def find_case(slug):
    return get_verified_case(slug) or get_case(slug)


def is_bookmarked(user_id, kind, slug):
    conn = connect()
    try:
        row = conn.execute(
            "SELECT 1 FROM bookmarks WHERE user_id = ? AND kind = ? AND slug = ?",
            (user_id, kind, slug),
        ).fetchone()
        return row is not None
    finally:
        conn.close()


@app.route("/")
def home():
    return render_template(
        "index.html", subjects=SUBJECTS[:6], cases=all_cases(),
        verified=VERIFIED_CASES, plans=PLANS,
    )


@app.route("/subjects")
def subjects():
    return render_template("subjects.html", subjects=SUBJECTS)


@app.route("/subjects/<slug>")
def subject_detail(slug):
    subject = get_subject(slug)
    if subject is None:
        abort(404)
    related = [c for c in all_cases() if c["subject"] == subject["name"]]
    user = current_user()
    bookmarked = is_bookmarked(user["id"], "subject", slug) if user else False
    return render_template("subject.html", subject=subject, related=related, bookmarked=bookmarked)


def court_group(court):
    # Order matters: Tuffour's court string mentions both the Supreme
    # Court and the Court of Appeal; it is a Supreme Court decision.
    if "Supreme Court" in court:
        return "supreme"
    if "Court of Appeal" in court:
        return "appeal"
    if "High Court" in court:
        return "high"
    return ""


@app.route("/cases")
def cases():
    subject_slug = request.args.get("subject", "")
    court = request.args.get("court", "")
    q = request.args.get("q", "").strip().lower()
    subject = get_subject(subject_slug) if subject_slug else None
    verified = VERIFIED_CASES
    if subject_slug:
        if subject:
            verified = [c for c in verified if c["subject"] == subject["name"]]
        else:
            verified = []
    if court:
        verified = [c for c in verified if court_group(c.get("court", "")) == court]
    if q:
        verified = [
            c for c in verified
            if q in c["title"].lower() or q in c.get("citation", "").lower()
            or q in c["principle"].lower()
        ]
    filtering = bool(subject_slug or court or q)
    return render_template(
        "cases.html", cases=CASES, verified=verified, subjects=SUBJECTS,
        subject_slug=subject_slug, court=court, q=request.args.get("q", ""),
        filtering=filtering, count=len(verified),
    )


@app.route("/cases/<slug>")
def case_detail(slug):
    case = find_case(slug)
    if case is None:
        abort(404)
    user = current_user()
    bookmarked = is_bookmarked(user["id"], "case", slug) if user else False
    return render_template("case.html", case=case, bookmarked=bookmarked)


@app.route("/search")
def search_page():
    query = request.args.get("q", "")
    subjects, practice = search_data(query) if query.strip() else ([], [])
    q = query.strip().lower()
    verified = [
        c for c in VERIFIED_CASES
        if q and (q in c["title"].lower() or q in c["subject"].lower()
                  or q in c.get("citation", "").lower() or q in c["principle"].lower()
                  or q in c.get("court", "").lower() or q in c["issue"].lower()
                  or q in c["rule"].lower() or q in c["facts"].lower())
    ] if q else []
    return render_template(
        "search.html", query=query, subjects=subjects, cases=practice, verified=verified
    )


@app.route("/plans")
def plans():
    return render_template("plans.html", plans=PLANS)


@app.route("/pay")
def pay():
    return render_template("pay.html")


# --- Accounts ---

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        if not name or not email or len(password) < 8:
            flash("Please give your name, email, and a password of at least 8 characters.")
            return render_template("register.html")
        conn = connect()
        try:
            conn.execute(
                "INSERT INTO users (email, name, password_hash) VALUES (?, ?, ?)",
                (email, name, generate_password_hash(password)),
            )
            conn.commit()
            row = conn.execute("SELECT id FROM users WHERE email = ?", (email,)).fetchone()
            session["user_id"] = row["id"]
        except Exception:
            conn.rollback()
            flash("That email is already registered. Try logging in instead.")
            return render_template("register.html")
        finally:
            conn.close()
        flash("Welcome to LexStudy Ghana. Your account is ready.")
        return redirect(url_for("account"))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        conn = connect()
        try:
            row = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
        finally:
            conn.close()
        if row and check_password_hash(row["password_hash"], password):
            session["user_id"] = row["id"]
            flash("Welcome back.")
            return redirect(url_for("account"))
        flash("That email or password did not match. Please try again.")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("user_id", None)
    flash("You have logged out.")
    return redirect(url_for("home"))


@app.route("/account")
@login_required
def account():
    user = current_user()
    conn = connect()
    try:
        bookmarks = conn.execute(
            "SELECT kind, slug FROM bookmarks WHERE user_id = ? ORDER BY id DESC", (user["id"],)
        ).fetchall()
        quiz_attempts = conn.execute(
            "SELECT quiz_slug, score, total, created_at FROM quiz_attempts WHERE user_id = ? ORDER BY id DESC LIMIT 20",
            (user["id"],),
        ).fetchall()
        irac_attempts = conn.execute(
            "SELECT scenario_slug, created_at FROM irac_attempts WHERE user_id = ? ORDER BY id DESC LIMIT 20",
            (user["id"],),
        ).fetchall()
        mock_attempts = conn.execute(
            "SELECT mock_slug, score, total, created_at FROM mock_attempts WHERE user_id = ? ORDER BY id DESC LIMIT 20",
            (user["id"],),
        ).fetchall()
        flashcard_rows = conn.execute(
            "SELECT card_id, due FROM flashcard_reviews WHERE user_id = ?", (user["id"],)
        ).fetchall()
    finally:
        conn.close()
    today = date.today().isoformat()
    reviewed_ids = {r["card_id"] for r in flashcard_rows}
    total_cards = len(all_cards())
    flashcard_summary = {
        "reviewed": len(reviewed_ids),
        "total": total_cards,
        "due": sum(1 for r in flashcard_rows if r["due"] <= today)
        + (total_cards - len(reviewed_ids)),
    }
    bookmark_items = []
    for b in bookmarks:
        if b["kind"] == "case":
            case = find_case(b["slug"])
            if case:
                bookmark_items.append(("Case brief", case["title"], f"/cases/{b['slug']}"))
        else:
            subject = get_subject(b["slug"])
            if subject:
                bookmark_items.append(("Subject", subject["name"], f"/subjects/{b['slug']}"))
    return render_template(
        "account.html", user=user, bookmark_items=bookmark_items,
        quiz_attempts=quiz_attempts, irac_attempts=irac_attempts, quizzes=QUIZZES,
        scenarios=SCENARIOS, mock_attempts=mock_attempts,
        flashcard_summary=flashcard_summary,
        mocks={m["slug"]: m for m in all_mocks()},
    )


@app.route("/bookmark/<kind>/<slug>", methods=["POST"])
@login_required
def bookmark(kind, slug):
    if kind not in ("case", "subject"):
        abort(404)
    if kind == "case" and not find_case(slug):
        abort(404)
    if kind == "subject" and not get_subject(slug):
        abort(404)
    user = current_user()
    conn = connect()
    try:
        existing = conn.execute(
            "SELECT 1 FROM bookmarks WHERE user_id = ? AND kind = ? AND slug = ?",
            (user["id"], kind, slug),
        ).fetchone()
        if existing:
            conn.execute(
                "DELETE FROM bookmarks WHERE user_id = ? AND kind = ? AND slug = ?",
                (user["id"], kind, slug),
            )
            flash("Bookmark removed.")
        else:
            conn.execute(
                "INSERT INTO bookmarks (user_id, kind, slug) VALUES (?, ?, ?)",
                (user["id"], kind, slug),
            )
            flash("Bookmarked. You can find it on your account page.")
        conn.commit()
    finally:
        conn.close()
    target = f"/cases/{slug}" if kind == "case" else f"/subjects/{slug}"
    return redirect(target)


# --- Quizzes ---

@app.route("/quizzes")
def quizzes():
    return render_template("quizzes.html", quizzes=QUIZZES)


@app.route("/quizzes/<slug>", methods=["GET", "POST"])
def quiz_detail(slug):
    quiz = get_quiz(slug)
    if quiz is None:
        abort(404)
    if request.method == "POST":
        questions = quiz["questions"]
        score = 0
        results = []
        for i, question in enumerate(questions):
            try:
                chosen = int(request.form.get(f"q{i}", -1))
            except ValueError:
                chosen = -1
            correct = chosen == question["answer"]
            score += 1 if correct else 0
            results.append({"question": question, "chosen": chosen, "correct": correct})
        user = current_user()
        if user:
            conn = connect()
            try:
                conn.execute(
                    "INSERT INTO quiz_attempts (user_id, quiz_slug, score, total) VALUES (?, ?, ?, ?)",
                    (user["id"], slug, score, len(questions)),
                )
                conn.commit()
            finally:
                conn.close()
        return render_template(
            "quiz_result.html", quiz=quiz, results=results, score=score, total=len(questions)
        )
    return render_template("quiz.html", quiz=quiz, slug=slug)


# --- IRAC trainer ---

@app.route("/irac")
def irac_index():
    return render_template("irac.html", scenarios=SCENARIOS)


@app.route("/irac/<slug>", methods=["GET", "POST"])
def irac_scenario(slug):
    scenario = get_scenario(slug)
    if scenario is None:
        abort(404)
    if request.method == "POST":
        issue = request.form.get("issue", "").strip()
        rule = request.form.get("rule", "").strip()
        application = request.form.get("application", "").strip()
        conclusion = request.form.get("conclusion", "").strip()
        user = current_user()
        if user:
            conn = connect()
            try:
                conn.execute(
                    "INSERT INTO irac_attempts (user_id, scenario_slug, issue, rule, application, conclusion) VALUES (?, ?, ?, ?, ?, ?)",
                    (user["id"], slug, issue, rule, application, conclusion),
                )
                conn.commit()
            finally:
                conn.close()
        return render_template(
            "irac_result.html", scenario=scenario,
            student={"issue": issue, "rule": rule, "application": application, "conclusion": conclusion},
        )
    return render_template("irac_scenario.html", scenario=scenario, slug=slug)


# --- Flashcards ---

def grade_card(ease, interval, reviews, grade):
    """Simple SM-2-style step. Returns (ease, interval_days, reviews).

    Again: ease drops, the card comes back today. Good: the interval
    grows by the ease factor. Easy: the interval grows faster and the
    ease rises a little. Ease stays between 1.3 and 2.5.
    """
    if grade == "again":
        return max(1.3, ease - 0.2), 0, reviews + 1
    if grade == "good":
        new_interval = 1 if reviews == 0 else max(1, round(interval * ease))
        return ease, new_interval, reviews + 1
    new_interval = 3 if reviews == 0 else max(1, round(interval * ease * 1.3))
    return min(2.5, ease + 0.15), new_interval, reviews + 1


def due_cards(user_id, slug, deck):
    """Cards due for review, in deck order, excluding cards already
    graded in this browser session. Returns (queue, reviews_by_id).
    Logged-out users have no saved reviews, so every card is due.
    """
    reviews = {}
    if user_id:
        conn = connect()
        try:
            rows = conn.execute(
                "SELECT card_id, due, ease, interval_days, reviews FROM flashcard_reviews WHERE user_id = ? AND deck_slug = ?",
                (user_id, slug),
            ).fetchall()
        finally:
            conn.close()
        reviews = {r["card_id"]: r for r in rows}
    today = date.today().isoformat()
    graded = set(session.get("graded_cards", []))
    queue = []
    for card in deck["cards"]:
        if card["id"] in graded:
            continue
        row = reviews.get(card["id"])
        if row is None or row["due"] <= today:
            queue.append(card)
    return queue, reviews


@app.route("/flashcards")
def flashcards_index():
    user = current_user()
    due_counts = {}
    if user:
        conn = connect()
        try:
            rows = conn.execute(
                "SELECT deck_slug, card_id, due FROM flashcard_reviews WHERE user_id = ?",
                (user["id"],),
            ).fetchall()
        finally:
            conn.close()
        today = date.today().isoformat()
        graded = set(session.get("graded_cards", []))
        for slug, deck in FLASHCARD_DECKS.items():
            reviewed = {r["card_id"]: r["due"] for r in rows if r["deck_slug"] == slug}
            due_counts[slug] = sum(
                1 for card in deck["cards"]
                if card["id"] not in graded
                and (card["id"] not in reviewed or reviewed[card["id"]] <= today)
            )
    else:
        due_counts = {slug: len(deck["cards"]) for slug, deck in FLASHCARD_DECKS.items()}
    return render_template(
        "flashcards.html", decks=FLASHCARD_DECKS, due_counts=due_counts
    )


@app.route("/flashcards/<slug>")
def flashcard_review(slug):
    deck = get_deck(slug)
    if deck is None:
        abort(404)
    user = current_user()
    queue, reviews = due_cards(user["id"] if user else None, slug, deck)
    card_id = request.args.get("card", "")
    card = next((c for c in queue if c["id"] == card_id), None) if card_id else None
    if card is None:
        card = queue[0] if queue else None
    return render_template(
        "flashcard_review.html", deck=deck, slug=slug, card=card,
        remaining=len(queue), total=len(deck["cards"]),
        show=request.args.get("show") == "1", reviews=reviews,
    )


@app.route("/flashcards/<slug>/grade", methods=["POST"])
def flashcard_grade(slug):
    deck = get_deck(slug)
    if deck is None:
        abort(404)
    card_id = request.form.get("card_id", "")
    grade = request.form.get("grade", "")
    if grade not in ("again", "good", "easy"):
        abort(400)
    if not any(c["id"] == card_id for c in deck["cards"]):
        abort(404)
    graded = session.get("graded_cards", [])
    if card_id not in graded:
        graded.append(card_id)
        session["graded_cards"] = graded
    user = current_user()
    if user:
        conn = connect()
        try:
            row = conn.execute(
                "SELECT ease, interval_days, reviews FROM flashcard_reviews WHERE user_id = ? AND card_id = ?",
                (user["id"], card_id),
            ).fetchone()
            if row:
                ease, interval, reviews = row["ease"], row["interval_days"], row["reviews"]
            else:
                ease, interval, reviews = 2.5, 0, 0
            ease, interval, reviews = grade_card(ease, interval, reviews, grade)
            due = (date.today() + timedelta(days=interval)).isoformat()
            if row:
                conn.execute(
                    "UPDATE flashcard_reviews SET ease = ?, interval_days = ?, due = ?, reviews = ?, last_grade = ?, deck_slug = ? WHERE user_id = ? AND card_id = ?",
                    (ease, interval, due, reviews, grade, slug, user["id"], card_id),
                )
            else:
                conn.execute(
                    "INSERT INTO flashcard_reviews (user_id, card_id, deck_slug, ease, interval_days, due, reviews, last_grade) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                    (user["id"], card_id, slug, ease, interval, due, reviews, grade),
                )
            conn.commit()
        finally:
            conn.close()
    return redirect(url_for("flashcard_review", slug=slug))


# --- Timed mocks ---

@app.route("/mocks")
def mocks_index():
    return render_template(
        "mocks.html", mocks=all_mocks(), time_limit=TIME_LIMIT_MINUTES
    )


@app.route("/mocks/<slug>", methods=["GET", "POST"])
def mock_detail(slug):
    mock = get_mock(slug)
    if mock is None:
        abort(404)
    if request.method == "POST":
        questions = mock["questions"]
        score = 0
        results = []
        for i, question in enumerate(questions):
            try:
                chosen = int(request.form.get(f"q{i}", -1))
            except ValueError:
                chosen = -1
            correct = chosen == question["answer"]
            score += 1 if correct else 0
            results.append({"question": question, "chosen": chosen, "correct": correct})
        user = current_user()
        if user:
            conn = connect()
            try:
                conn.execute(
                    "INSERT INTO mock_attempts (user_id, mock_slug, score, total) VALUES (?, ?, ?, ?)",
                    (user["id"], slug, score, len(questions)),
                )
                conn.commit()
            finally:
                conn.close()
        return render_template(
            "mock_result.html", mock=mock, results=results, score=score, total=len(questions)
        )
    return render_template(
        "mock.html", mock=mock, slug=slug, time_limit=TIME_LIMIT_MINUTES
    )


@app.route("/health")
def health():
    return {"status": "ok", "service": "lexstudy-ghana", "version": "0.3"}


@app.route("/manifest.json")
def manifest():
    return app.send_static_file("manifest.json")


@app.errorhandler(404)
def not_found(_error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
