# Backend foundation

## Current scope

The isolated backend includes a Flask application factory, SQLAlchemy, Flask-Migrate integration, API versioning, liveness and readiness endpoints, cookie-session authentication foundations, CSRF protection, role assignments, audit events and rate limiting.

## Initial endpoints

- GET /api/v1/health: process liveness.
- GET /api/v1/ready: database readiness.
- GET /api/v1/auth/csrf: issue a session-bound CSRF token.
- POST /api/v1/auth/register: create a student account.
- POST /api/v1/auth/login: authenticate a user.
- POST /api/v1/auth/logout: terminate the session.
- GET /api/v1/auth/me: return the current user's public profile.

All state-changing API requests require the X-CSRF-Token header. The token is issued by the CSRF endpoint and rotated after login or registration. Browser authentication uses the Flask signed session cookie, configured as HTTP-only and SameSite=Lax. SESSION_COOKIE_SECURE defaults to true. Set it to false only for local HTTP development.

## Data isolation

The initial identity models use the table prefix legum_ (legum_users, legum_roles, legum_user_roles and legum_audit_logs). This is deliberate. The legacy application already has a users table with a different schema. The new backend must not collide with or alter legacy tables while the data mapping and migration plan are being prepared.

These are development models, not yet the production migration. Before any migration, inspect a schema-only dump from the actual production database and map legacy user identifiers, password hashes, bookmarks and learning attempts.

## Rate limiting

Flask-Limiter is configured. Its default memory storage is suitable only for local development or a single-process test. A production multi-worker deployment must configure RATELIMIT_STORAGE_URI to a shared Redis-compatible service. Do not rely on per-process memory counters for production abuse prevention.

## Known next work

- Add email verification and password reset flows.
- Add persistent session revocation and account recovery.
- Add role administration and permission policies.
- Configure shared production rate-limit storage.
- Add structured request logging.
- Generate and review Alembic migrations from a verified schema baseline.
- Add integration tests against PostgreSQL in CI.
- Add login abuse monitoring and account recovery controls.
- Add explicit privacy and data-retention rules.
