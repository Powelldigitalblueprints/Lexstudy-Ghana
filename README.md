# LexStudy Ghana — v0.1

Working name for a new, independent Ghanaian legal studies platform.
Separate from Powell Digital Blueprints: own code, own repository,
own Render service and database. Nothing in this project reads or
writes Powell data.

## What v0.1 does

- Homepage with subjects and practice briefs
- Course catalogue: 8 subjects, each with topics and study notes
- Case brief library: 4 practice briefs in IRAC structure
- Search across subjects, notes and briefs
- Plans page: Free / Monthly / Annual (prices to be confirmed;
  payments are NOT connected in v0.1)
- Health check at `/health`

## What v0.1 does NOT do yet

- Student registration, login, saved notes or progress tracking
- Paid-content restrictions
- Payment processing (Paystack / MoMo / crypto — none connected)
- Real, citable case briefs

## Accuracy rule

The briefs in v0.1 are PRACTICE briefs on hypothetical facts. They
teach IRAC and must never be cited as real cases. Any real brief
added later must be verified against the authoritative judgment
first, with its citation, before publication. This site is a study
aid, not legal advice.

## Run locally

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python app.py
```

Then open http://127.0.0.1:5000

## Deploy (next step, not done in v0.1)

1. Create a new private GitHub repository named `lexstudy-ghana`
   (do not initialise it with a README).
2. Push this code to that repository.
3. In Render, create a new web service from that repository, or use
   the Blueprint in `render.yaml` (creates the web service and a
   separate `lexstudy-ghana-db` PostgreSQL database).
4. Verify: homepage loads, a subject page loads, search returns a
   result, `/health` returns `{"status": "ok", ...}`.
5. Only then move to v0.2: accounts, verified real briefs, quizzes,
   IRAC practice, and payment connection.
