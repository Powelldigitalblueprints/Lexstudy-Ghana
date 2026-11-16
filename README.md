# LexStudy Ghana — v0.3.5

Working name for a new, independent Ghanaian legal studies platform.
Separate from Powell Digital Blueprints: own code, own repository,
own Render service and database. Nothing in this project reads or
writes Powell data.

## What v0.3.5 does

- Homepage with subjects, cited briefs and practice briefs
- Course catalogue: 8 subjects, each with topics and study notes
- Case brief library, split clearly:
  - 12 cited briefs of real cases, with citation, court, date and
    sources checked (see VERIFICATION-LOG.md for what was checked
    and when); the brief index filters by subject, court and
    title/citation/principle
  - 4 practice briefs on hypothetical facts, in IRAC structure
- Case Library: 12 full case files (same cases as the cited briefs),
  each with material facts, procedural history, issues, holding, ratio
  decidendi kept separate from obiter, reasoning, order made, why it
  matters, legislation and cases considered, and sources checked;
  searchable by name, citation, court, topic and principle, with a
  request-a-case flow for cases not yet covered. The paid gate exists
  (CASE_LIBRARY_GATE) but is off until payments connect; pro access
  never expires in v0.3.4
- Owner-only case requests view at /admin/requests: lists every
  requested case with the requester and date, plus a most-requested
  summary. Visible only to the account whose email matches the
  LEXSTUDY_OWNER_EMAIL environment variable (unset: nobody can see it)
- Accounts: register, log in, log out, with hashed passwords
- Bookmarks for subjects and briefs, shown on the account page
- Quizzes: Constitutional Law and Legal System and Methods
  (10 questions each), Contract and Tort (5 questions each), with
  explanations; scores are saved when logged in
- Flashcards: one deck per subject, 5 cards each (Constitutional Law
  has 13, Legal System and Methods has 21), with Again/Good/Easy
  grading and simple
  spaced-repetition intervals; progress is saved per account, with
  a due-today queue
- Timed mocks: one 10-minute timed mock per quiz subject (the
  Constitutional Law and Legal System and Methods mocks have 10
  questions, the others 5), with a countdown and auto-submit;
  scores are saved when logged in and shown on the account page
- IRAC trainer: 5 hypothetical scenarios; students write their own
  IRAC and compare with a model answer and self-check list
- Search across subjects, notes, cited briefs and practice briefs;
  cited briefs match on citation, court, issue, rule, facts and
  principle as well as title and subject
- Plans page: Free / Monthly / Annual (prices to be confirmed;
  payments are NOT connected in v0.3.5)
- Basic PWA: manifest, icon and a service worker that caches
  static assets only (not full offline notes yet)
- Health check at `/health` (version 0.3.5)

## What v0.3.5 does NOT do yet

- Paid-content restrictions: the Case Library gate exists but is
off, so all content is currently free to browse; no UI grants pro
access yet, and pro access never expires in v0.3.4
- Payment processing (Paystack / MoMo — none connected; see /pay)
- Full offline notes
- A research database of full judgments (cited briefs here are
  summaries, not full judgment text)

## Accuracy rule

Practice briefs use hypothetical facts and must never be cited as
real cases. Cited briefs are summaries checked against the public
sources listed on each brief page. They are not reproductions of
full judgments, and they are not a substitute for reading the
reported judgment before citing a case in court work. If a detail
here conflicts with the reported judgment, the reported judgment
prevails. Case Library files are fuller study summaries with the
same standing. This site is a study aid, not legal advice.

## Run locally

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python app.py
```

Then open http://127.0.0.1:5000

Set SECRET_KEY in the environment for production. The local SQLite
database file (lexstudy.db) is ignored by git and must not be
committed.

## Deploy (live in a separate Render account)

The service is live at lexstudy-ghana-zdt9.onrender.com, in a Render
account separate from Powell's. PostgreSQL support (v0.2.1): when
DATABASE_URL is set, accounts, bookmarks and attempts are stored in
PostgreSQL and survive redeploys; without it, the app falls back to
local SQLite. The Render service needs DATABASE_URL set from its own
free PostgreSQL database (lexstudy-ghana-db) in that same account —
do not point it at any Powell database. Tables are created
automatically by CREATE TABLE IF NOT EXISTS on first run. v0.3.4
adds the Case Library (new module case_library.py, /library routes,
pro_access and case_requests tables); the gate stays off unless
CASE_LIBRARY_GATE=on is set in Render. v0.3.5 adds the owner-only
/admin/requests view (no schema changes; set LEXSTUDY_OWNER_EMAIL in
Render to the owner's account email to use it). No dependency changes.


## Past Questions Archive — Phase 1

The Phase 1 foundation adds institution, course and examination-paper metadata
tables for both PostgreSQL and SQLite. It adds a public searchable listing,
paper detail pages for external links, and an owner-only administration page
for registering institutions, LLB courses and examination records.

New records remain drafts by default. Publication is restricted to external
links with a checked source and an explicit link or distribution status.
Hosted PDF storage is represented in the schema but is not enabled until a
private object-storage provider is configured. No PDFs are stored in Git.

### Local tests

Run the isolated Phase 1 regression suite with:

```bash
python -m unittest discover -s tests -v
```

The tests create a temporary SQLite database and do not use production data.

### Routes

- `/past-questions` — published examination archive and filters
- `/past-questions/<slug>` — source-linked examination record
- `/admin/past-questions` — owner-only institution, course and paper management

Set `LEXSTUDY_OWNER_EMAIL` to the site owner's registered account email to
enable archive administration. The existing `LEXSTUDY_OWNER_EMAIL` setting
is reused. No payment or subscription behaviour is changed.
