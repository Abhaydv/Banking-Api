import uuid

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_check():
    # Given the banking API is running
    # When we call the health endpoint
    response = client.get("/health")

    # Then the API should be healthy
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_register_user():
    # Given a new user
    user = {
        "full_name": "BDD Test User",
        "email": f"bddtest_{uuid.uuid4().hex[:8]}@example.com",
        "password": "Password@123"
    }

    # When we register the user
    response = client.post(
        "/api/v1/auth/register",
        json=user
    )

    # Then registration should succeed
    assert response.status_code == 201
    assert response.json()["email"] == user["email"]


def test_login_user():
    # Given an existing user
    user = {
        "full_name": "Login Test User",
        "email": f"logintest_{uuid.uuid4().hex[:8]}@example.com",
        "password": "Password@123"
    }

    client.post(
        "/api/v1/auth/register",
        json=user
    )

    # When the user logs in
    response = client.post(
        "/api/v1/auth/login",
        json={
            "email": user["email"],
            "password": user["password"]
        }
    )

    # Then a JWT token should be returned
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"