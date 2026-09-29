# 🏦 Banking API

A secure and modular RESTful Banking API built with **Python, FastAPI, SQLAlchemy, SQLite, and JWT authentication**.

The project provides core banking operations such as user registration, authentication, account management, deposits, withdrawals, fund transfers, and transaction history.

---

## 🚀 Features

- User registration and login
- Secure password hashing using bcrypt
- JWT-based authentication
- Protected API endpoints
- User profile management
- Bank account creation
- Multiple accounts per user
- Account balance management
- Deposit money
- Withdraw money
- Fund transfer between accounts
- Transaction history
- Account ownership validation
- Request validation using Pydantic
- HTTP exception handling
- SQLAlchemy ORM
- Modular service-layer architecture
- Interactive Swagger API documentation

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend programming |
| FastAPI | REST API framework |
| SQLAlchemy | ORM and database interaction |
| SQLite | Relational database |
| Pydantic | Request/response validation |
| JWT | Authentication |
| Passlib + bcrypt | Password hashing |
| Uvicorn | ASGI server |
| Git & GitHub | Version control |

---

## 📁 Project Structure

```text
Banking-Api/
│
├── app/
│   ├── api/
│   │   ├── deps.py
│   │   └── routes/
│   │       ├── auth.py
│   │       ├── users.py
│   │       ├── accounts.py
│   │       └── transactions.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   └── exceptions.py
│   │
│   ├── database/
│   │   └── database.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   ├── account.py
│   │   └── transaction.py
│   │
│   ├── schemas/
│   │   ├── auth.py
│   │   ├── user.py
│   │   ├── account.py
│   │   └── transaction.py
│   │
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── account_service.py
│   │   └── transaction_service.py
│   │
│   └── main.py
│
├── tests/
├── .gitignore
├── README.md
└── requirements.txt
