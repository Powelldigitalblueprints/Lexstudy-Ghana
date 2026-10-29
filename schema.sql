-- LexStudy Ghana — PostgreSQL schema for v0.2 (accounts, content, progress).
-- v0.2 runs accounts, bookmarks, quiz attempts and IRAC attempts on
-- SQLite locally (db.py) with this same table shape; PostgreSQL
-- wiring for Render is a deployment step, not a content change.
-- Do NOT load real case briefs into cases until each one is verified
-- against its authoritative judgment. Practice briefs stay flagged is_practice=true.

CREATE TABLE IF NOT EXISTS subjects (
  id SERIAL PRIMARY KEY,
  slug TEXT UNIQUE NOT NULL,
  name TEXT NOT NULL,
  level TEXT NOT NULL,
  description TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS notes (
  id SERIAL PRIMARY KEY,
  subject_id INTEGER REFERENCES subjects(id),
  title TEXT NOT NULL,
  summary TEXT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS cases (
  id SERIAL PRIMARY KEY,
  slug TEXT UNIQUE NOT NULL,
  title TEXT NOT NULL,
  subject TEXT NOT NULL,
  is_practice BOOLEAN NOT NULL DEFAULT TRUE,
  verified_against_judgment BOOLEAN NOT NULL DEFAULT FALSE,
  citation TEXT,
  facts TEXT NOT NULL,
  issue TEXT NOT NULL,
  rule TEXT NOT NULL,
  application TEXT NOT NULL,
  conclusion TEXT NOT NULL,
  principle TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  email TEXT UNIQUE NOT NULL,
  password_hash TEXT NOT NULL,
  plan TEXT NOT NULL DEFAULT 'free',
  created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS saved_notes (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id),
  note_id INTEGER REFERENCES notes(id),
  UNIQUE (user_id, note_id)
);

CREATE TABLE IF NOT EXISTS bookmarks (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id),
  kind TEXT NOT NULL,
  slug TEXT NOT NULL,
  UNIQUE (user_id, kind, slug),
  created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS quiz_attempts (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id),
  quiz_slug TEXT NOT NULL,
  score INTEGER NOT NULL,
  total INTEGER NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS irac_attempts (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id),
  scenario_slug TEXT NOT NULL,
  issue TEXT NOT NULL,
  rule TEXT NOT NULL,
  application TEXT NOT NULL,
  conclusion TEXT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW()
);
