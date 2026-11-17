def test_health_endpoint_reports_api_process_status(client):
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.get_json() == {
        "status": "ok",
        "service": "legum-api",
        "version": "0.1.0",
    }


def test_readiness_endpoint_checks_database(client):
    response = client.get("/api/v1/ready")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ready"
