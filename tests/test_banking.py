from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def create_and_login():
    user = {
        "full_name": "Banking Test User",
        "email": "bankingtest@example.com",
        "password": "Password@123"
    }

    client.post(
        "/api/v1/auth/register",
        json=user
    )

    response = client.post(
        "/api/v1/auth/login",
        json={
            "email": user["email"],
            "password": user["password"]
        }
    )

    return response.json()["access_token"]


def test_create_account():
    # Given a logged-in user
    token = create_and_login()

    headers = {
        "Authorization": f"Bearer {token}"
    }

    # When the user creates a savings account
    response = client.post(
        "/api/v1/accounts",
        json={"account_type": "SAVINGS"},
        headers=headers
    )

    # Then the account should be created
    assert response.status_code == 201
    assert response.json()["account_type"] == "SAVINGS"
    assert response.json()["balance"] == 0


def test_deposit():
    # Given a logged-in user with an account
    token = create_and_login()

    headers = {
        "Authorization": f"Bearer {token}"
    }

    account_response = client.post(
        "/api/v1/accounts",
        json={"account_type": "SAVINGS"},
        headers=headers
    )

    account_id = account_response.json()["id"]

    # When the user deposits money
    response = client.post(
        f"/api/v1/accounts/{account_id}/deposit",
        json={"amount": 1000},
        headers=headers
    )

    # Then the deposit should succeed
    assert response.status_code == 200
    assert response.json()["transaction_type"] == "DEPOSIT"
    assert response.json()["amount"] == 1000


def test_withdraw():
    # Given an account with money
    token = create_and_login()

    headers = {
        "Authorization": f"Bearer {token}"
    }

    account_response = client.post(
        "/api/v1/accounts",
        json={"account_type": "SAVINGS"},
        headers=headers
    )

    account_id = account_response.json()["id"]

    client.post(
        f"/api/v1/accounts/{account_id}/deposit",
        json={"amount": 1000},
        headers=headers
    )

    # When the user withdraws money
    response = client.post(
        f"/api/v1/accounts/{account_id}/withdraw",
        json={"amount": 500},
        headers=headers
    )

    # Then the withdrawal should succeed
    assert response.status_code == 200
    assert response.json()["transaction_type"] == "WITHDRAW"
    assert response.json()["amount"] == 500


def test_insufficient_balance():
    # Given an account with no money
    token = create_and_login()

    headers = {
        "Authorization": f"Bearer {token}"
    }

    account_response = client.post(
        "/api/v1/accounts",
        json={"account_type": "SAVINGS"},
        headers=headers
    )

    account_id = account_response.json()["id"]

    # When the user tries to withdraw more than the balance
    response = client.post(
        f"/api/v1/accounts/{account_id}/withdraw",
        json={"amount": 500},
        headers=headers
    )

    # Then the request should be rejected
    assert response.status_code == 400
    assert response.json()["detail"] == "Insufficient balance"


def test_transaction_history():
    # Given an account with a deposit
    token = create_and_login()

    headers = {
        "Authorization": f"Bearer {token}"
    }

    account_response = client.post(
        "/api/v1/accounts",
        json={"account_type": "SAVINGS"},
        headers=headers
    )

    account_id = account_response.json()["id"]

    client.post(
        f"/api/v1/accounts/{account_id}/deposit",
        json={"amount": 1000},
        headers=headers
    )

    # When transaction history is requested
    response = client.get(
        f"/api/v1/accounts/{account_id}/transactions",
        headers=headers
    )

    # Then the transaction should be returned
    assert response.status_code == 200
    assert len(response.json()) >= 1
    assert response.json()[0]["transaction_type"] == "DEPOSIT"


def test_protected_endpoint_without_token():
    # When accessing a protected endpoint without authentication
    response = client.get("/api/v1/accounts")

    # Then access should be denied
    assert response.status_code == 401