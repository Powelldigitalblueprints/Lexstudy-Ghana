import pytest

from app import create_app


def test_application_refuses_to_start_without_secret_key():
    with pytest.raises(RuntimeError, match="SECRET_KEY"):
        create_app({
            "TESTING": False,
            "SECRET_KEY": None,
            "SQLALCHEMY_DATABASE_URI": "sqlite://",
        })


def test_session_cookie_security_defaults_to_explicit_secure_setting():
    app = create_app({
        "TESTING": True,
        "SECRET_KEY": "test-secret",
        "SQLALCHEMY_DATABASE_URI": "sqlite://",
        "SESSION_COOKIE_SECURE": True,
    })
    assert app.config["SESSION_COOKIE_HTTPONLY"] is True
    assert app.config["SESSION_COOKIE_SECURE"] is True
    assert app.config["SESSION_COOKIE_SAMESITE"] == "Lax"


def test_api_sets_basic_security_headers(client):
    response = client.get("/api/v1/health")
    assert response.headers["X-Content-Type-Options"] == "nosniff"
    assert response.headers["X-Frame-Options"] == "DENY"
    assert response.headers["Referrer-Policy"] == "strict-origin-when-cross-origin"
