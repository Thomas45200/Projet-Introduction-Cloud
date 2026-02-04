from app.main import app

def test_api_events():
    client = app.test_client()
    response = client.get("/api/events")
    assert response.status_code == 200
    assert "items" in response.get_json()

def test_api_news():
    client = app.test_client()
    response = client.get("/api/news")
    assert response.status_code == 200
    assert "items" in response.get_json()

def test_api_faq():
    client = app.test_client()
    response = client.get("/api/faq")
    assert response.status_code == 200
    assert "items" in response.get_json()
