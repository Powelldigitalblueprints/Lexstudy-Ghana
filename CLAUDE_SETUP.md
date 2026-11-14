# Claude API setup for Legum / LexStudy Ghana

The premium AI tutor is available at `/ai` and `POST /api/ai/chat`. Both routes
require a signed-in account with an existing `pro_access` record. The default
allowance is 25 requests per user per day, controlled by `CLAUDE_LEGUM_DAILY_LIMIT`.

Set these variables on the separate LexStudy Ghana Render service:

- `ANTHROPIC_API_KEY`: a Legum-specific Anthropic API key, separate from Powell.
- `CLAUDE_ENABLED=true`: enable the tutor after the key is set.
- `CLAUDE_MODEL=claude-sonnet-5-5`: default tutor model.
- `CLAUDE_LEGUM_DAILY_LIMIT=25`: daily premium request limit.

The feature does not grant premium access. It relies on the existing `pro_access`
table. The current application README states that payment processing is not connected,
so subscription payment and automatic pro-access granting must be completed separately
before selling this feature as part of a paid plan.

Legal answers are educational study assistance. The tutor is instructed not to invent
citations or holdings and to distinguish hypothetical scenarios from real cases.
Do not put the API key in source control.
