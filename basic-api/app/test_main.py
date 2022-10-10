from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/helloworld")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_read_healthcheck():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "UP"}
