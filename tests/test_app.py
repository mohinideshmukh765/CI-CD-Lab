import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"CI/CD Pipeline &amp; Monitoring Lab" in response.data or b"CI/CD Pipeline & Monitoring Lab" in response.data
    assert b"Shivam Korpade" in response.data
    assert b"2324000756" in response.data

def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data is not None
    assert json_data["status"] == "UP"
    assert "uptime_seconds" in json_data
    assert "timestamp" in json_data
    assert json_data["version"] == "1.0.0"

def test_metrics_endpoint(client):
    response = client.get("/metrics")
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data is not None
    assert "total_requests" in json_data
    assert "python_version" in json_data

def test_info_endpoint(client):
    response = client.get("/info")
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["author"] == "Shivam Korpade"
    assert json_data["prn"] == "2324000756"

def test_not_found(client):
    response = client.get("/non-existent-route")
    assert response.status_code == 404
    json_data = response.get_json()
    assert json_data["code"] == 404
