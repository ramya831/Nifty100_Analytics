from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)


def test_sectors():
    response = client.get("/api/v1/sectors/sectors/")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)