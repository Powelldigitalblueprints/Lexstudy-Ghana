# Legacy data map and migration controls

## Scope and evidence

This is a source-derived map of the schema declared in the legacy `db.py`. It is not a claim that the current Render PostgreSQL instance has been inspected. Production schema confirmation requires a read-only metadata report from that database.

The source defines eight operational tables:

| Legacy table | Declared fields and purpose | Proposed destination |
|---|---|---|
| `users` | id, email, name, password_hash, created_at | `legum_users` |
| `bookmarks` | id, user_id, kind, slug, created_at | New bookmark model, preserving IDs and uniqueness |
| `quiz_attempts` | id, user_id, quiz_slug, score, total, created_at | Learning assessment records |
| `irac_attempts` | id, user_id, scenario_slug, issue, rule, application, conclusion, created_at | IRAC submissions |
| `flashcard_reviews` | id, user_id, card_id, deck_slug, ease, interval_days, due, reviews, last_grade, updated_at | Flashcard review records |
| `mock_attempts` | id, user_id, mock_slug, score, total, created_at | Mock examination attempts |
| `pro_access` | id, user_id, granted_at | Legacy entitlement history, requiring expiry policy |
| `case_requests` | id, user_id, case_name, citation, notes, created_at | Case research requests |

The Claude feature branch also creates a daily usage table at runtime. It is not part of the eight-table main-branch schema and must be checked separately if that branch has ever been deployed.

## Source inconsistencies requiring production verification

1. `db.py` declares `users.name`, but the checked-in `schema.sql` reference declares `users.plan` and omits `name`.
2. `schema.sql` includes `subjects`, `notes`, `cases` and `saved_notes`, which are not created by the operational `db.py` schema.
3. `db.py` creates `pro_access` and `case_requests`, which are absent from the checked-in `schema.sql`.
4. Both operational database dialects use `CREATE TABLE IF NOT EXISTS`. This does not upgrade existing table definitions.
5. The actual production schema may differ from both source definitions due to prior manual changes or deployed feature branches.

## Identity migration rules

- Preserve each legacy user ID in a dedicated `legacy_user_id` mapping column or migration map. Do not assume IDs can be regenerated safely.
- Normalize email addresses only after checking for case-insensitive duplicates.
- Preserve the existing Werkzeug password hash string exactly during initial migration. Verify compatibility against the deployed Werkzeug version before cutover. Rehash after a successful login if the stored hash uses an older supported method.
- Do not mark existing accounts email-verified unless evidence supports that status.
- Preserve original account creation timestamps.
- Do not silently merge duplicate accounts.

The new development identity models use the `legum_` table prefix to avoid colliding with the legacy `users` table while migration work is underway.

## Learning data migration rules

- Preserve primary keys and user foreign-key relationships wherever practical.
- Preserve all quiz, IRAC and mock attempt scores and timestamps.
- Preserve flashcard ease, interval, due date, review count and last grade exactly.
- Preserve bookmark kind and slug values. Validate each slug against the new content catalogue before enabling the migrated bookmark UI.
- Preserve case requests and requester relationships. Do not expose administrative request data to ordinary users.
- Treat `pro_access` as historical access evidence. It has no expiry in the legacy design, so it must not automatically become a permanent paid subscription in the new billing model.

## Read-only schema inspection

The script `backend/scripts/inspect_legacy_schema.py` accepts a dedicated `LEGACY_DATABASE_URL`. It reads PostgreSQL metadata only and starts a read-only transaction. It does not select application records or write to the database.

Run it only after confirming that the URL points to the intended Legum database:

```bash
cd backend
export LEGACY_DATABASE_URL="postgresql://..."
python scripts/inspect_legacy_schema.py --output legacy-schema-report.json
```

Do not commit the connection string or the generated report if it contains internal database naming details. Share the report through an approved private channel for migration planning.

## Cutover prerequisites

No production migration should be generated or applied until all of the following are complete:

1. Obtain a verified production backup and test restoration.
2. Capture the actual production schema metadata.
3. Confirm whether the Claude branch has been deployed and whether its usage table exists.
4. Compare source-derived schema, actual production schema and destination models.
5. Write explicit, reversible migration steps with row-count and relationship checks.
6. Test the migration against a restored, sanitised database copy.
7. Rehearse rollback and define a maintenance window.
8. Obtain explicit approval before production execution.
