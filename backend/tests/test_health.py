from app import create_app


def test_health_endpoint_reports_api_process_status():
    app = create_app({
        "TESTING": True,
        "SECRET_KEY": "test-secret",
        "SQLALCHEMY_DATABASE_URI": "sqlite://",
    })
    response = app.test_client().get("/api/v1/health")
    assert response.status_code == 200
    assert response.get_json() == {
        "status": "ok",
        "service": "legum-api",
        "version": "0.1.0",
    }
