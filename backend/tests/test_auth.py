def test_registration_creates_student_account_and_session(client, csrf):
    response = client.post(
        "/api/v1/auth/register",
        json={"name": "Ama Student", "email": "AMA@example.com", "password": "Correct-Horse-42"},
        headers={"X-CSRF-Token": csrf},
    )
    assert response.status_code == 201
    body = response.get_json()
    assert body["user"]["email"] == "ama@example.com"
    assert body["user"]["roles"] == ["student"]
    assert body["csrf_token"]
    assert client.get("/api/v1/auth/me").get_json()["user"]["name"] == "Ama Student"


def test_registration_rejects_short_password(client, csrf):
    response = client.post(
        "/api/v1/auth/register",
        json={"name": "Ama", "email": "ama@example.com", "password": "short"},
        headers={"X-CSRF-Token": csrf},
    )
    assert response.status_code == 400
    assert response.get_json()["error"]["code"] == "weak_password"


def test_registration_rejects_duplicate_email(client, registered_user):
    csrf = client.get("/api/v1/auth/csrf").get_json()["csrf_token"]
    response = client.post(
        "/api/v1/auth/register",
        json={"name": "Another Student", "email": "STUDENT@example.com", "password": "Correct-Horse-42"},
        headers={"X-CSRF-Token": csrf},
    )
    assert response.status_code == 409


def test_login_and_logout(client, registered_user):
    client.post("/api/v1/auth/logout", headers={"X-CSRF-Token": registered_user["csrf_token"]})
    token = client.get("/api/v1/auth/csrf").get_json()["csrf_token"]
    response = client.post(
        "/api/v1/auth/login",
        json={"email": "student@example.com", "password": "Correct-Horse-42"},
        headers={"X-CSRF-Token": token},
    )
    assert response.status_code == 200
    login_body = response.get_json()
    assert login_body["user"]["email"] == "student@example.com"
    logout = client.post("/api/v1/auth/logout", headers={"X-CSRF-Token": login_body["csrf_token"]})
    assert logout.status_code == 200
    assert client.get("/api/v1/auth/me").status_code == 401


def test_login_rejects_invalid_credentials(client, registered_user):
    token = client.get("/api/v1/auth/csrf").get_json()["csrf_token"]
    response = client.post(
        "/api/v1/auth/login",
        json={"email": "student@example.com", "password": "wrong-password"},
        headers={"X-CSRF-Token": token},
    )
    assert response.status_code == 401


def test_state_changing_request_requires_csrf(client):
    response = client.post("/api/v1/auth/logout")
    assert response.status_code == 403


def test_authenticated_endpoint_requires_login(client):
    response = client.get("/api/v1/auth/me")
    assert response.status_code == 401
