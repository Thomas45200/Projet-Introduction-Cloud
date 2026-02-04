from app.main import app

def test_healthz_returns_ok():
    client = app.test_client()
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"

def test_readyz_returns_ready():
    client = app.test_client()
    response = client.get("/readyz")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ready"
