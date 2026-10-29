-- LexStudy Ghana — PostgreSQL schema for v0.2 (accounts, content, progress).
-- v0.1 runs on the seeded content in data.py; this schema is ready, not yet wired up.
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
