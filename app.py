"""LexStudy Ghana v0.2 — accounts, verified briefs, quizzes, IRAC.

Accounts in v0.2 are for bookmarks and progress only. All content is
currently free to browse; paid-content restrictions are NOT yet
enforced, and no payment provider is connected. Passwords are hashed
with Werkzeug and never stored in plain text. The database file is
local (SQLite, see db.py) and must not be committed.
"""

import os
from functools import wraps

from flask import (
    Flask, abort, flash, g, redirect, render_template, request,
    session, url_for,
)
from werkzeug.security import check_password_hash, generate_password_hash

from data import CASES, PLANS, SUBJECTS, get_case, get_subject, search as search_data
from db import connect, init_db
from irac_data import SCENARIOS, get_scenario
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


@app.route("/cases")
def cases():
    return render_template("cases.html", cases=CASES, verified=VERIFIED_CASES)


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
                  or q in c.get("citation", "").lower() or q in c["principle"].lower())
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
    finally:
        conn.close()
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
        scenarios=SCENARIOS,
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


@app.route("/health")
def health():
    return {"status": "ok", "service": "lexstudy-ghana", "version": "0.2"}


@app.route("/manifest.json")
def manifest():
    return app.send_static_file("manifest.json")


@app.errorhandler(404)
def not_found(_error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
