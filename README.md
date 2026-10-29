# LexStudy Ghana — v0.2

Working name for a new, independent Ghanaian legal studies platform.
Separate from Powell Digital Blueprints: own code, own repository,
own Render service and database. Nothing in this project reads or
writes Powell data.

## What v0.2 does

- Homepage with subjects, cited briefs and practice briefs
- Course catalogue: 8 subjects, each with topics and study notes
- Case brief library, split clearly:
  - 3 cited briefs of real cases, with citation, court, date and
    sources checked (Tuffour v Attorney-General [1980] GLR 637;
    NPP v Attorney-General [1993-94] 2 GLR 35, the 31 December case;
    Re Akoto [1961] GLR 523)
  - 4 practice briefs on hypothetical facts, in IRAC structure
- Accounts: register, log in, log out, with hashed passwords
- Bookmarks for subjects and briefs, shown on the account page
- Quizzes: Constitutional Law, Contract and Tort, 5 questions each,
  with explanations; scores are saved when logged in
- IRAC trainer: 3 hypothetical scenarios; students write their own
  IRAC and compare with a model answer and self-check list
- Search across subjects, notes, cited briefs and practice briefs
- Plans page: Free / Monthly / Annual (prices to be confirmed;
  payments are NOT connected in v0.2)
- Basic PWA: manifest, icon and a service worker that caches
  static assets only (not full offline notes yet)
- Health check at `/health` (version 0.2)

## What v0.2 does NOT do yet

- Paid-content restrictions: all content is currently free to browse
- Payment processing (Paystack / MoMo — none connected; see /pay)
- Full offline notes, spaced-repetition flashcards, timed mocks
- A research database of full judgments (cited briefs here are
  summaries, not full judgment text)

## Accuracy rule

Practice briefs use hypothetical facts and must never be cited as
real cases. Cited briefs are summaries checked against the public
sources listed on each brief page. They are not reproductions of
full judgments, and they are not a substitute for reading the
reported judgment before citing a case in court work. If a detail
here conflicts with the reported judgment, the reported judgment
prevails. This site is a study aid, not legal advice.

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

## Deploy (paused — not done in v0.2)

The v0.1 code is already in GitHub at
Powelldigitalblueprints/Lexstudy-Ghana (public, main, v0.1 commit).
v0.2 has NOT been pushed or deployed yet. When pushing, verify the
file list and the health endpoint after deployment, and remember
that Render deployment needs the PostgreSQL wiring step in
schema.sql, since v0.2 still uses SQLite locally.
