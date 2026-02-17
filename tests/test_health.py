from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")

    # Assert status code
    assert response.status_code == 200

    # Assert exact JSON response
    assert response.json() == {"status": "ok"}

