from fastapi import FastAPI

from app.database.database import engine, Base
from app.models import User, Account, Transaction

from app.api.routes.auth import router as auth_router
from app.api.routes.users import router as users_router
from app.api.routes.accounts import router as accounts_router
from app.api.routes.transactions import router as transactions_router


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Banking API",
    description="Basic Banking Application REST API",
    version="1.0.0"
)


app.include_router(auth_router)
app.include_router(users_router)
app.include_router(accounts_router)
app.include_router(transactions_router)


@app.get("/")
def root():
    return {
        "message": "Banking API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }