-- LexStudy Ghana — PostgreSQL schema reference for v0.3.
-- The live schema is created by db.py (CREATE TABLE IF NOT EXISTS)
-- in both SQLite and PostgreSQL; this file is a reference copy of
-- the PostgreSQL shape, including the content tables not yet used
-- by the app (subjects, notes, cases).
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

CREATE TABLE IF NOT EXISTS flashcard_reviews (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id),
  card_id TEXT NOT NULL,
  deck_slug TEXT NOT NULL,
  ease REAL NOT NULL DEFAULT 2.5,
  interval_days INTEGER NOT NULL DEFAULT 0,
  due TEXT NOT NULL,
  reviews INTEGER NOT NULL DEFAULT 0,
  last_grade TEXT,
  updated_at TIMESTAMPTZ DEFAULT NOW(),
  UNIQUE (user_id, card_id)
);

CREATE TABLE IF NOT EXISTS mock_attempts (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id),
  mock_slug TEXT NOT NULL,
  score INTEGER NOT NULL,
  total INTEGER NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW()
);
