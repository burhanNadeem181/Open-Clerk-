from fastapi.testclient import TestClient
from app.main import app
import app.database as database


def test_create_and_list_lead(tmp_path, monkeypatch):
    test_db = tmp_path / "test.db"
    monkeypatch.setattr(database, "DB_PATH", test_db)

    with TestClient(app) as client:
        response = client.post(
            "/leads",
            json={
                "name": "Ayesha Khan",
                "email": "ayesha@example.com",
                "business": "Example Clinic",
                "message": "I am ready to book this week.",
            },
        )
        assert response.status_code == 201
        assert response.json()["priority"] == "high"

        listed = client.get("/leads")
        assert listed.status_code == 200
        assert len(listed.json()) == 1
        assert listed.json()[0]["email"] == "ayesha@example.com"


def test_health_endpoint():
    with TestClient(app) as client:
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json()["status"] == "ok"
