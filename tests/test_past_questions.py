"""Read-only-safe regression tests for the Past Questions Phase 1 module.

Run with: python -m unittest discover -s tests -v
The suite always uses a temporary SQLite database and never connects to
the configured production database.
"""
import os
import re
import tempfile
import unittest

_TEST_DIR = tempfile.TemporaryDirectory(prefix="lexstudy-pq-tests-")
os.environ["LEXSTUDY_DB"] = os.path.join(_TEST_DIR.name, "test.db")
os.environ.pop("DATABASE_URL", None)
os.environ["LEXSTUDY_OWNER_EMAIL"] = "owner@example.test"

from werkzeug.security import generate_password_hash
import app as application


class PastQuestionsPhaseOneTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        application.app.config.update(TESTING=True, SECRET_KEY="test-secret")

    def setUp(self):
        self.client = application.app.test_client()
        conn = application.connect()
        try:
            conn.execute("DELETE FROM exam_papers")
            conn.execute("DELETE FROM exam_courses")
            conn.execute("DELETE FROM institutions")
            conn.execute("DELETE FROM users")
            conn.commit()
            conn.execute(
                "INSERT INTO users (email, name, password_hash) VALUES (?, ?, ?)",
                ("owner@example.test", "Test Owner", generate_password_hash("test-password")),
            )
            conn.commit()
            row = conn.execute("SELECT id FROM users WHERE email = ?", ("owner@example.test",)).fetchone()
            self.owner_id = row["id"]
        finally:
            conn.close()

    def _owner_session(self):
        with self.client.session_transaction() as state:
            state["user_id"] = self.owner_id

    def _csrf(self):
        response = self.client.get("/admin/past-questions")
        self.assertEqual(response.status_code, 200)
        with self.client.session_transaction() as state:
            return state["_pq_csrf"]

    def test_schema_is_additive_and_contains_archive_tables(self):
        conn = application.connect()
        try:
            names = {r["name"] for r in conn.execute(
                "SELECT name FROM sqlite_master WHERE type = 'table'"
            ).fetchall()}
            self.assertTrue({"users", "bookmarks", "quiz_attempts", "institutions",
                             "exam_courses", "exam_papers"}.issubset(names))
        finally:
            conn.close()

    def test_existing_homepage_and_health_still_work(self):
        self.assertEqual(self.client.get("/").status_code, 200)
        self.assertEqual(self.client.get("/health").json["version"], "0.3.5")

    def test_admin_requires_owner_and_csrf(self):
        self.assertEqual(self.client.get("/admin/past-questions").status_code, 403)
        self._owner_session()
        token = self._csrf()
        response = self.client.post("/admin/past-questions", data={
            "action": "institution", "name": "Test University"
        })
        self.assertEqual(response.status_code, 400)
        self.assertTrue(token)

    def test_full_metadata_flow_and_publication_checks(self):
        self._owner_session()
        token = self._csrf()
        headers = {"_csrf_token": token}

        response = self.client.post("/admin/past-questions", data={
            **headers, "action": "institution", "name": "Test University",
            "abbreviation": "TU", "website_url": "https://university.example"
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        conn = application.connect()
        try:
            institution = conn.execute(
                "SELECT id FROM institutions WHERE slug = 'test-university'"
            ).fetchone()
        finally:
            conn.close()
        self.assertIsNotNone(institution)

        response = self.client.post("/admin/past-questions", data={
            **headers, "action": "course", "institution_id": str(institution["id"]),
            "course_code": "LLB 101", "course_title": "Constitutional Law",
            "academic_level": "Level 100", "subject_name": "Constitutional Law",
            "subject_slug": "constitutional-law", "programme": "LLB"
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        conn = application.connect()
        try:
            course = conn.execute("SELECT id FROM exam_courses WHERE course_code = 'LLB 101'").fetchone()
        finally:
            conn.close()
        self.assertIsNotNone(course)

        self.client.post("/admin/past-questions", data={
            **headers, "action": "paper", "course_id": str(course["id"]),
            "academic_year": "2025/2026", "semester": "First Semester",
            "examination_type": "End-of-semester", "paper_title": "Constitutional Law Examination",
            "access_mode": "external", "source_url": "https://university.example/papers/llb101.pdf",
            "source_attribution": "Test University", "verification_status": "source_checked",
            "rights_status": "link_only", "verification_notes": "Original university source checked"
        }, follow_redirects=True)

        conn = application.connect()
        try:
            paper = conn.execute("SELECT id, slug, publication_status FROM exam_papers").fetchone()
        finally:
            conn.close()
        self.assertIsNotNone(paper)
        self.assertEqual(paper["publication_status"], "draft")

        response = self.client.post("/admin/past-questions", data={
            **headers, "action": "publish", "paper_id": str(paper["id"])
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.client.get("/past-questions").status_code, 200)
        self.assertEqual(self.client.get("/past-questions/" + paper["slug"]).status_code, 200)

    def test_unverified_or_restricted_paper_cannot_publish(self):
        self._owner_session()
        token = self._csrf()
        conn = application.connect()
        try:
            conn.execute(
                "INSERT INTO institutions (slug, name) VALUES (?, ?)",
                ("restricted-university", "Restricted University"),
            )
            institution = conn.execute(
                "SELECT id FROM institutions WHERE slug = ?", ("restricted-university",)
            ).fetchone()
            conn.execute(
                """INSERT INTO exam_courses
                   (institution_id, course_code, course_title, academic_level)
                   VALUES (?, ?, ?, ?)""",
                (institution["id"], "LAW100", "Law", "Level 100"),
            )
            course = conn.execute("SELECT id FROM exam_courses WHERE course_code = 'LAW100'").fetchone()
            conn.execute(
                """INSERT INTO exam_papers
                   (slug, course_id, academic_year, semester, examination_type, paper_title,
                    access_mode, source_url, verification_status, rights_status)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                ("restricted-paper", course["id"], "2025/2026", "First Semester",
                 "End-of-semester", "Restricted Paper", "external",
                 "https://university.example/paper.pdf", "unverified", "restricted"),
            )
            conn.commit()
            paper = conn.execute("SELECT id FROM exam_papers WHERE slug = 'restricted-paper'").fetchone()
        finally:
            conn.close()
        self.client.post("/admin/past-questions", data={
            "_csrf_token": token, "action": "publish", "paper_id": str(paper["id"])
        }, follow_redirects=True)
        conn = application.connect()
        try:
            status = conn.execute(
                "SELECT publication_status FROM exam_papers WHERE id = ?", (paper["id"],)
            ).fetchone()["publication_status"]
        finally:
            conn.close()
        self.assertEqual(status, "draft")


if __name__ == "__main__":
    unittest.main()
