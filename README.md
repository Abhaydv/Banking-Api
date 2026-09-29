# 🏦 Banking API

A RESTful Banking API built with **Python, FastAPI, SQLAlchemy, SQLite, JWT authentication, and pytest**.

The project demonstrates how to build a secure backend for basic banking operations such as user registration, authentication, account management, deposits, withdrawals, transfers, and transaction history.

---

## 🚀 Features

- User registration and login
- Password hashing using bcrypt
- JWT-based authentication
- Protected API endpoints
- JWT token revocation on logout
- User-specific account access
- Savings and Current account types
- Account creation
- Deposit money
- Withdraw money
- Account-to-account transfers
- Transaction history
- Insufficient balance validation
- Account status validation
- Input validation using Pydantic
- SQLAlchemy ORM
- SQLite database
- Decimal-based money handling
- Database commit/rollback handling
- Environment-based configuration
- Swagger/OpenAPI documentation
- Automated API tests using pytest

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| FastAPI | REST API framework |
| SQLAlchemy | ORM and database interaction |
| SQLite | Relational database |
| Pydantic | Request/response validation |
| Pydantic Settings | Environment configuration |
| JWT | Authentication |
| Passlib + bcrypt | Password hashing |
| Uvicorn | ASGI server |
| Pytest | Automated testing |
| Git & GitHub | Version control |

---

## 📁 Project Structure

```text
banking-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   ├── deps.py
│   │   └── routes/
│   │       ├── __init__.py
│   │       ├── auth.py
│   │       ├── users.py
│   │       ├── accounts.py
│   │       └── transactions.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── security.py
│   │   └── exceptions.py
│   │
│   ├── database/
│   │   ├── __init__.py
│   │   └── database.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── account.py
│   │   └── transaction.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── user.py
│   │   ├── account.py
│   │   └── transaction.py
│   │
│   └── services/
│       ├── __init__.py
│       ├── auth_service.py
│       ├── account_service.py
│       └── transaction_service.py
│
├── tests/
│   ├── __init__.py
│   ├── test_auth.py
│   └── test_banking.py
│
├── .env
├── .gitignore
├── README.md
├── requirements.txt
└── banking.db
