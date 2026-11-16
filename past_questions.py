"""Phase 1 foundation for the LexStudy Ghana Past Questions Archive.

This module manages archive metadata only. Hosted object-storage integration
and PDF delivery are intentionally deferred until storage credentials and
distribution rights have been configured.
"""
import re
from datetime import datetime, timezone
from urllib.parse import urlparse
from uuid import uuid4

from flask import Blueprint, abort, flash, redirect, render_template, request, session, url_for
from markupsafe import escape
import secrets
import hmac


bp = Blueprint("past_questions", __name__)


def slugify(value):
    value = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return value[:150] or "exam-paper"


def valid_http_url(value):
    try:
        parsed = urlparse(value.strip())
        return parsed.scheme in ("http", "https") and bool(parsed.netloc)
    except (TypeError, ValueError):
        return False


def register_routes(app, connect, current_user, is_owner):
    """Register archive routes using the application's existing DB/auth layer."""

    @bp.context_processor
    def archive_context():
        token = session.get("_pq_csrf")
        if not token:
            token = secrets.token_urlsafe(32)
            session["_pq_csrf"] = token
        return {"pq_csrf_token": token}

    @bp.before_request
    def protect_archive_posts():
        if request.method == "POST":
            expected = session.get("_pq_csrf", "")
            supplied = request.form.get("_csrf_token", "")
            if not expected or not supplied or not hmac.compare_digest(expected, supplied):
                abort(400, description="Invalid form security token.")

    def require_owner():
        user = current_user()
        if not user or not is_owner(user):
            abort(403)
        return user

    @bp.route("/past-questions")
    def index():
        filters = {
            "institution": request.args.get("institution", "").strip(),
            "level": request.args.get("level", "").strip(),
            "subject": request.args.get("subject", "").strip(),
            "year": request.args.get("year", "").strip(),
            "semester": request.args.get("semester", "").strip(),
            "q": request.args.get("q", "").strip(),
        }
        sql = """SELECT p.id, p.slug, p.paper_title, p.academic_year, p.semester,
                        p.examination_type, p.access_mode, c.course_code, c.course_title,
                        c.academic_level, c.subject_name, i.name AS institution_name
                 FROM exam_papers p
                 JOIN exam_courses c ON c.id = p.course_id
                 JOIN institutions i ON i.id = c.institution_id
                 WHERE p.publication_status = 'published' AND i.is_active = 1"""
        params = []
        for field, column in (
            ("institution", "i.slug"), ("level", "c.academic_level"),
            ("subject", "c.subject_slug"), ("year", "p.academic_year"),
            ("semester", "p.semester"),
        ):
            if filters[field]:
                sql += f" AND {column} = ?"
                params.append(filters[field])
        if filters["q"]:
            sql += """ AND (LOWER(p.paper_title) LIKE ? OR LOWER(c.course_title) LIKE ?
                       OR LOWER(c.course_code) LIKE ? OR LOWER(i.name) LIKE ?)"""
            term = "%" + filters["q"].lower() + "%"
            params.extend([term, term, term, term])
        sql += " ORDER BY p.academic_year DESC, i.name, c.course_code LIMIT 200"
        conn = connect()
        try:
            papers = [dict(row) for row in conn.execute(sql, tuple(params)).fetchall()]
            institutions = [dict(row) for row in conn.execute(
                "SELECT slug, name FROM institutions WHERE is_active = 1 ORDER BY name"
            ).fetchall()]
            levels = [r["academic_level"] for r in conn.execute(
                "SELECT DISTINCT academic_level FROM exam_courses ORDER BY academic_level"
            ).fetchall()]
            years = [r["academic_year"] for r in conn.execute(
                "SELECT DISTINCT academic_year FROM exam_papers WHERE publication_status = 'published' ORDER BY academic_year DESC"
            ).fetchall()]
        finally:
            conn.close()
        return render_template("past_questions.html", papers=papers, institutions=institutions,
                               levels=levels, years=years, filters=filters)

    @bp.route("/past-questions/<slug>")
    def detail(slug):
        conn = connect()
        try:
            row = conn.execute(
                """SELECT p.*, c.course_code, c.course_title, c.academic_level,
                          c.subject_name, i.name AS institution_name
                   FROM exam_papers p JOIN exam_courses c ON c.id = p.course_id
                   JOIN institutions i ON i.id = c.institution_id
                   WHERE p.slug = ? AND p.publication_status = 'published' AND i.is_active = 1""",
                (slug,),
            ).fetchone()
        finally:
            conn.close()
        if not row:
            abort(404)
        paper = dict(row)
        if paper["access_mode"] == "external" and valid_http_url(paper["source_url"]):
            return render_template("past_question_detail.html", paper=paper)
        # Private hosted files are not served until the object-storage adapter is installed.
        abort(404)

    @bp.route("/admin/past-questions", methods=["GET", "POST"])
    def admin():
        user = require_owner()
        if request.method == "POST":
            action = request.form.get("action", "")
            conn = connect()
            try:
                if action == "institution":
                    name = request.form.get("name", "").strip()
                    abbreviation = request.form.get("abbreviation", "").strip()
                    website = request.form.get("website_url", "").strip()
                    if not name or (website and not valid_http_url(website)):
                        flash("Enter an institution name and a valid website URL.")
                    else:
                        slug = slugify(request.form.get("slug", "") or name)
                        conn.execute(
                            "INSERT INTO institutions (slug, name, abbreviation, website_url) VALUES (?, ?, ?, ?)",
                            (slug, name, abbreviation, website),
                        )
                        conn.commit()
                        flash("Institution added.")
                elif action == "course":
                    institution_id = int(request.form.get("institution_id", "0"))
                    code = request.form.get("course_code", "").strip()
                    title = request.form.get("course_title", "").strip()
                    level = request.form.get("academic_level", "").strip()
                    subject_slug = slugify(request.form.get("subject_slug", "").strip()) if request.form.get("subject_slug", "").strip() else ""
                    subject_name = request.form.get("subject_name", "").strip()
                    programme = request.form.get("programme", "LLB").strip() or "LLB"
                    if not code or not title or level not in ("Level 100", "Level 200", "Level 300", "Level 400"):
                        flash("Provide a course code, title and valid LLB academic level.")
                    else:
                        conn.execute(
                            """INSERT INTO exam_courses
                               (institution_id, course_code, course_title, subject_slug, subject_name, academic_level, programme)
                               VALUES (?, ?, ?, ?, ?, ?, ?)""",
                            (institution_id, code, title, subject_slug, subject_name, level, programme),
                        )
                        conn.commit()
                        flash("Course added.")
                elif action == "paper":
                    course_id = int(request.form.get("course_id", "0"))
                    year = request.form.get("academic_year", "").strip()
                    semester = request.form.get("semester", "").strip()
                    exam_type = request.form.get("examination_type", "").strip()
                    title = request.form.get("paper_title", "").strip()
                    access_mode = request.form.get("access_mode", "external").strip()
                    source_url = request.form.get("source_url", "").strip()
                    attribution = request.form.get("source_attribution", "").strip()
                    verification = request.form.get("verification_status", "unverified").strip()
                    rights = request.form.get("rights_status", "pending").strip()
                    notes = request.form.get("verification_notes", "").strip()
                    allowed_semesters = ("First Semester", "Second Semester", "Trimester", "Other")
                    allowed_types = ("Mid-semester", "End-of-semester", "Resit", "Supplementary", "Other")
                    allowed_verification = ("unverified", "source_checked", "institution_confirmed")
                    allowed_rights = ("pending", "permission_granted", "open_licence", "link_only", "restricted")
                    valid = (year and re.fullmatch(r"\d{4}/\d{4}", year)
                             and semester in allowed_semesters and exam_type in allowed_types
                             and title and access_mode in ("external", "hosted")
                             and verification in allowed_verification and rights in allowed_rights)
                    if not valid:
                        flash("Check the academic year, semester, examination type and document details.")
                    elif access_mode == "external" and not valid_http_url(source_url):
                        flash("An externally linked paper requires a valid HTTP or HTTPS source URL.")
                    elif access_mode == "hosted":
                        flash("Hosted uploads are not enabled yet. Phase 1 records hosted-storage fields, while secure storage is implemented in a later phase.")
                    else:
                        base = slugify(title + "-" + year + "-" + semester)
                        slug = base + "-" + uuid4().hex[:8]
                        conn.execute(
                            """INSERT INTO exam_papers
                               (slug, course_id, academic_year, semester, examination_type, paper_title,
                                access_mode, source_url, source_attribution, verification_status,
                                rights_status, verification_notes, uploaded_by)
                               VALUES (?, ?, ?, ?, ?, ?, 'external', ?, ?, ?, ?, ?, ?)""",
                            (slug, course_id, year, semester, exam_type, title, source_url,
                             attribution, verification, rights, notes, user["id"]),
                        )
                        conn.commit()
                        flash("Examination record saved as a draft. Review its source and distribution status before publishing.")
                elif action == "publish":
                    paper_id = int(request.form.get("paper_id", "0"))
                    row = conn.execute(
                        "SELECT access_mode, source_url, verification_status, rights_status FROM exam_papers WHERE id = ?",
                        (paper_id,),
                    ).fetchone()
                    if not row:
                        abort(404)
                    paper = dict(row)
                    eligible = (paper["access_mode"] == "external"
                                and valid_http_url(paper["source_url"])
                                and paper["verification_status"] in ("source_checked", "institution_confirmed")
                                and paper["rights_status"] in ("permission_granted", "open_licence", "link_only"))
                    if not eligible:
                        flash("This paper cannot be published. Verify its source and confirm that linking or distribution is permitted.")
                    else:
                        conn.execute(
                            "UPDATE exam_papers SET publication_status = 'published', verified_by = ?, verified_at = ?, updated_at = ? WHERE id = ?",
                            (user["id"], datetime.now(timezone.utc).isoformat(), datetime.now(timezone.utc).isoformat(), paper_id),
                        )
                        conn.commit()
                        flash("Paper published.")
                elif action == "withdraw":
                    paper_id = int(request.form.get("paper_id", "0"))
                    conn.execute(
                        "UPDATE exam_papers SET publication_status = 'withdrawn', updated_at = ? WHERE id = ?",
                        (datetime.now(timezone.utc).isoformat(), paper_id),
                    )
                    conn.commit()
                    flash("Paper withdrawn.")
                else:
                    abort(400)
            except ValueError:
                conn.rollback()
                flash("A numeric record identifier was expected.")
            except Exception:
                conn.rollback()
                raise
            finally:
                conn.close()
            return redirect(url_for("past_questions.admin"))

        conn = connect()
        try:
            institutions = [dict(r) for r in conn.execute(
                "SELECT * FROM institutions ORDER BY name"
            ).fetchall()]
            courses = [dict(r) for r in conn.execute(
                """SELECT c.*, i.name AS institution_name FROM exam_courses c
                   JOIN institutions i ON i.id = c.institution_id ORDER BY i.name, c.course_code"""
            ).fetchall()]
            papers = [dict(r) for r in conn.execute(
                """SELECT p.*, c.course_code, c.course_title, i.name AS institution_name
                   FROM exam_papers p JOIN exam_courses c ON c.id = p.course_id
                   JOIN institutions i ON i.id = c.institution_id
                   ORDER BY p.id DESC LIMIT 200"""
            ).fetchall()]
        finally:
            conn.close()
        return render_template("admin_past_questions.html", institutions=institutions,
                               courses=courses, papers=papers)

    app.register_blueprint(bp)
