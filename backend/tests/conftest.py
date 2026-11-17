import pytest

from app import create_app
from app.extensions import db


@pytest.fixture()
def app():
    application = create_app({
        "TESTING": True,
        "SECRET_KEY": "test-secret-key",
        "SQLALCHEMY_DATABASE_URI": "sqlite://",
        "SESSION_COOKIE_SECURE": False,
        "RATELIMIT_ENABLED": False,
    })
    with application.app_context():
        db.create_all()
        yield application
        db.session.remove()
        db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def csrf(client):
    response = client.get("/api/v1/auth/csrf")
    assert response.status_code == 200
    return response.get_json()["csrf_token"]


@pytest.fixture()
def registered_user(client):
    token = client.get("/api/v1/auth/csrf").get_json()["csrf_token"]
    response = client.post(
        "/api/v1/auth/register",
        json={"name": "Test Student", "email": "student@example.com", "password": "Correct-Horse-42"},
        headers={"X-CSRF-Token": token},
    )
    assert response.status_code == 201
    return response.get_json()
