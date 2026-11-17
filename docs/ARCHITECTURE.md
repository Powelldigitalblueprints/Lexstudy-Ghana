# Legum target architecture

## Status
Initial development scaffold. The legacy application has not yet been migrated.

## Application shape
- React and TypeScript provide the browser application.
- Flask exposes versioned JSON endpoints under /api/v1.
- PostgreSQL is the production relational database.
- SQLAlchemy maps application entities.
- Alembic, through Flask-Migrate, manages schema changes.
- Anthropic Claude is the initial AI model provider.
- Render remains the initial hosting platform.

The frontend and backend are kept in separate directories. The existing root-level Flask application remains intact during the transition.

## Backend boundaries
The Flask application will be divided into route blueprints, service modules, data models and validation schemas. Route handlers should remain thin. Business rules belong in services. Database access belongs behind well-defined model or repository operations.

## Security principles
- Fail closed when the production SECRET_KEY is missing.
- Enforce permissions on the server for every protected resource.
- Use secure, HTTP-only cookies and CSRF protection for browser sessions.
- Verify payment transactions with the provider before granting entitlements.
- Keep API credentials and database credentials in environment variables.
- Apply rate limits and usage controls to authentication and AI endpoints.
- Record administrative actions and payment events.

## Data migration principles
- Never point development or test environments at production data.
- Back up production before every schema migration.
- Use forward migrations with a documented rollback or recovery plan.
- Preserve legacy user identifiers and learning records where possible.
- Reconcile the operational schema in db.py before treating schema.sql as authoritative.
- Do not remove legacy routes until replacements pass acceptance tests.

## Deployment
The existing Render service and database remain the production system during development. The new frontend and backend must first be deployed to isolated staging resources. Production cutover requires explicit approval after data, security and acceptance tests pass.
