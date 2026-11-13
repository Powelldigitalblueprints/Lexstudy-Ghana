"""Database storage for LexStudy Ghana v0.2.1.

Two backends, one interface:

- PostgreSQL when DATABASE_URL is set (Render). This is the live
  backend: accounts, bookmarks and attempts survive redeploys.
- SQLite when DATABASE_URL is not set (local development). The file
  must NOT be committed (see .gitignore).

app.py only ever calls connect(), execute(), fetchone()/fetchall(),
commit(), rollback() and close(), and reads rows by column name, so
the wrapper below keeps both backends interchangeable. The only
differences it hides are the parameter placeholder (? for SQLite,
%s for PostgreSQL) and the schema dialect (AUTOINCREMENT /
datetime('now') vs SERIAL / NOW()).
"""

import os
import sqlite3

DB_PATH = os.environ.get("LEXSTUDY_DB", os.path.join(os.path.dirname(__file__), "lexstudy.db"))

SQLITE_SCHEMA = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TEXT DEFAULT (datetime('now'))
);
CREATE TABLE IF NOT EXISTS bookmarks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL REFERENCES users(id),
    kind TEXT NOT NULL,
    slug TEXT NOT NULL,
    created_at TEXT DEFAULT (datetime('now')),
    UNIQUE (user_id, kind, slug)
);
CREATE TABLE IF NOT EXISTS quiz_attempts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL REFERENCES users(id),
    quiz_slug TEXT NOT NULL,
    score INTEGER NOT NULL,
    total INTEGER NOT NULL,
    created_at TEXT DEFAULT (datetime('now'))
);
CREATE TABLE IF NOT EXISTS irac_attempts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL REFERENCES users(id),
    scenario_slug TEXT NOT NULL,
    issue TEXT NOT NULL,
    rule TEXT NOT NULL,
    application TEXT NOT NULL,
    conclusion TEXT NOT NULL,
    created_at TEXT DEFAULT (datetime('now'))
);
"""

PG_SCHEMA = """
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
CREATE TABLE IF NOT EXISTS bookmarks (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id),
    kind TEXT NOT NULL,
    slug TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE (user_id, kind, slug)
);
CREATE TABLE IF NOT EXISTS quiz_attempts (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id),
    quiz_slug TEXT NOT NULL,
    score INTEGER NOT NULL,
    total INTEGER NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
CREATE TABLE IF NOT EXISTS irac_attempts (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id),
    scenario_slug TEXT NOT NULL,
    issue TEXT NOT NULL,
    rule TEXT NOT NULL,
    application TEXT NOT NULL,
    conclusion TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
"""


def using_postgres():
    return bool(os.environ.get("DATABASE_URL"))


class _Cursor:
    def __init__(self, cursor):
        self._cursor = cursor

    def fetchone(self):
        return self._cursor.fetchone()

    def fetchall(self):
        return self._cursor.fetchall()


class _Connection:
    def __init__(self, conn, postgres):
        self._conn = conn
        self._postgres = postgres

    def execute(self, sql, params=()):
        if self._postgres:
            sql = sql.replace("?", "%s")
        cursor = self._conn.cursor()
        cursor.execute(sql, params)
        return _Cursor(cursor)

    def executescript(self, sql):
        if self._postgres:
            cursor = self._conn.cursor()
            cursor.execute(sql)
        else:
            self._conn.executescript(sql)

    def commit(self):
        self._conn.commit()

    def rollback(self):
        self._conn.rollback()

    def close(self):
        self._conn.close()


def connect():
    if using_postgres():
        import psycopg2
        from psycopg2.extras import RealDictCursor

        raw = psycopg2.connect(
            os.environ["DATABASE_URL"], cursor_factory=RealDictCursor
        )
        return _Connection(raw, postgres=True)
    raw = sqlite3.connect(DB_PATH)
    raw.row_factory = sqlite3.Row
    return _Connection(raw, postgres=False)


def init_db():
    conn = connect()
    try:
        conn.executescript(PG_SCHEMA if using_postgres() else SQLITE_SCHEMA)
        conn.commit()
    finally:
        conn.close()
