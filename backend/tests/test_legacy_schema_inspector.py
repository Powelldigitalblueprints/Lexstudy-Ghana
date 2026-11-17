import pytest

from scripts.inspect_legacy_schema import inspect_database


def test_schema_inspector_rejects_non_postgresql_urls():
    with pytest.raises(ValueError, match="Only PostgreSQL"):
        inspect_database("sqlite:///not-a-production-database.db")
