import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app({"TESTING": True, "TRUST_PROXY_HEADERS": False})
    return app.test_client()


def test_index(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.content_type == "text/html; charset=utf-8"
    assert b"Your Flask app is running" in response.data


def test_static_asset(client):
    response = client.get("/static/styles.css")

    assert response.status_code == 200
    assert response.content_type == "text/css; charset=utf-8"


def test_status(client):
    response = client.get("/api/status")

    assert response.status_code == 200
    assert response.json["status"] == "ok"
    assert response.json["framework"].startswith("Flask ")


def test_healthz(client):
    response = client.get("/healthz")

    assert response.status_code == 200
    assert response.json == {"status": "ok"}


def test_not_found(client):
    response = client.get("/missing")

    assert response.status_code == 404
    assert response.json == {"detail": "Not found"}


def test_method_not_allowed(client):
    response = client.post("/")

    assert response.status_code == 405
    assert response.json == {"detail": "Method not allowed"}
    assert "GET" in response.headers["Allow"]
