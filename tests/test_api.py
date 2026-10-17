from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_health():
    response = client.get("/health")
    assert response.json()["status"] == "healthy"


def test_prediction():
    response = client.post(
        "/predict",
        json={"text": "I love this wonderful product"},
    )
    assert response.status_code == 200
    assert response.json()["sentiment"] in ["positive", "negative"]


def test_short_text_rejected():
    response = client.post("/predict", json={"text": "a"})
    assert response.status_code == 422
