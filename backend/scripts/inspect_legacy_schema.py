"""Read-only PostgreSQL schema inspection for the legacy Legum database.

This utility reads metadata only. It never reads application rows or changes
the database. Supply LEGACY_DATABASE_URL explicitly and review the target
before running it.
"""
import argparse
import json
import os
import sys

from sqlalchemy import create_engine, inspect
from sqlalchemy.engine import make_url


def inspect_database(database_url):
    url = make_url(database_url)
    if url.drivername not in {"postgres", "postgresql", "postgresql+psycopg2"}:
        raise ValueError("Only PostgreSQL URLs are accepted for legacy inspection.")

    engine = create_engine(database_url, pool_pre_ping=True)
    try:
        with engine.connect() as connection:
            connection.exec_driver_sql("SET TRANSACTION READ ONLY")
            inspector = inspect(connection)
            report = {
                "database_dialect": engine.dialect.name,
                "metadata_only": True,
                "tables": [],
            }

            for table_name in sorted(inspector.get_table_names()):
                columns = []
                for column in inspector.get_columns(table_name):
                    columns.append({
                        "name": column["name"],
                        "type": str(column["type"]),
                        "nullable": column["nullable"],
                        "default": str(column["default"]) if column.get("default") is not None else None,
                    })

                report["tables"].append({
                    "name": table_name,
                    "columns": columns,
                    "primary_key": inspector.get_pk_constraint(table_name),
                    "foreign_keys": inspector.get_foreign_keys(table_name),
                    "unique_constraints": inspector.get_unique_constraints(table_name),
                    "indexes": inspector.get_indexes(table_name),
                })
            return report
    finally:
        engine.dispose()


def main():
    parser = argparse.ArgumentParser(description="Read PostgreSQL schema metadata without reading application data.")
    parser.add_argument("--output", help="Optional local JSON output path.")
    args = parser.parse_args()

    database_url = os.environ.get("LEGACY_DATABASE_URL")
    if not database_url:
        parser.error("Set LEGACY_DATABASE_URL to the legacy PostgreSQL connection string.")

    try:
        report = inspect_database(database_url)
    except Exception as exc:
        print(f"Schema inspection failed: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 1

    rendered = json.dumps(report, indent=2, default=str)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as output_file:
            output_file.write(rendered + "\n")
        print(f"Schema metadata written to {args.output}")
    else:
        print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
