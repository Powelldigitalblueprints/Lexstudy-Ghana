# Database migrations

This directory is reserved for Alembic migration scripts generated through Flask-Migrate.

From the backend directory, initialise migrations once with:

```bash
flask --app run.py db init
```

After importing and reviewing the complete model set, generate a migration:

```bash
flask --app run.py db migrate -m "Describe the schema change"
flask --app run.py db upgrade
```

Never run an upgrade against production until a verified backup exists and the migration has been tested against a restored, sanitised copy of production data. Review generated SQL before applying it. Do not use `db migrate` as a substitute for reviewing data-preservation requirements.
