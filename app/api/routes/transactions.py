from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.database.database import get_db
from app.models.user import User
from app.models.account import Account
from app.schemas.transaction import (
    DepositRequest,
    WithdrawRequest,
    TransactionResponse
)
from app.services.transaction_service import (
    deposit,
    withdraw,
    get_transactions
)


router = APIRouter(
    prefix="/api/v1/accounts",
    tags=["Transactions"]
)


def get_user_account(
    db: Session,
    account_id: int,
    user_id: int
):
    account = (
        db.query(Account)
        .filter(
            Account.id == account_id,
            Account.user_id == user_id
        )
        .first()
    )

    if account is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Account not found"
        )

    return account


@router.post(
    "/{account_id}/deposit",
    response_model=TransactionResponse
)
def deposit_money(
    account_id: int,
    data: DepositRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    account = get_user_account(
        db,
        account_id,
        current_user.id
    )

    return deposit(
        db,
        account,
        data.amount
    )


@router.post(
    "/{account_id}/withdraw",
    response_model=TransactionResponse
)
def withdraw_money(
    account_id: int,
    data: WithdrawRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    account = get_user_account(
        db,
        account_id,
        current_user.id
    )

    return withdraw(
        db,
        account,
        data.amount
    )


@router.get(
    "/{account_id}/transactions",
    response_model=List[TransactionResponse]
)
def transaction_history(
    account_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    account = get_user_account(
        db,
        account_id,
        current_user.id
    )

    return get_transactions(
        db,
        account.id
    )