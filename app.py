"""LexStudy Ghana v0.1 — Flask foundation.

Routes: home, subjects, subject detail, case library, case detail,
search, plans, health. No accounts, no payments, no paid-content
restrictions yet — those are v0.2. Data is seeded in data.py for v0.1;
schema.sql defines the PostgreSQL tables for the next stage.
"""

import os

from flask import Flask, abort, render_template, request

from data import CASES, PLANS, SUBJECTS, get_case, get_subject, search

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "index.html", subjects=SUBJECTS[:6], cases=CASES, plans=PLANS
    )


@app.route("/subjects")
def subjects():
    return render_template("subjects.html", subjects=SUBJECTS)


@app.route("/subjects/<slug>")
def subject_detail(slug):
    subject = get_subject(slug)
    if subject is None:
        abort(404)
    related = [c for c in CASES if c["subject"] == subject["name"]]
    return render_template("subject.html", subject=subject, related=related)


@app.route("/cases")
def cases():
    return render_template("cases.html", cases=CASES)


@app.route("/cases/<slug>")
def case_detail(slug):
    case = get_case(slug)
    if case is None:
        abort(404)
    return render_template("case.html", case=case)


@app.route("/search")
def search_page():
    query = request.args.get("q", "")
    subjects, cases = search(query) if query.strip() else ([], [])
    return render_template(
        "search.html", query=query, subjects=subjects, cases=cases
    )


@app.route("/plans")
def plans():
    return render_template("plans.html", plans=PLANS)


@app.route("/health")
def health():
    return {"status": "ok", "service": "lexstudy-ghana", "version": "0.1"}


@app.errorhandler(404)
def not_found(_error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
