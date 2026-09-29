from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.database.database import get_db
from app.models.user import User
from app.schemas.account import AccountCreate, AccountResponse
from app.services.account_service import (
    create_account,
    get_user_accounts
)


router = APIRouter(
    prefix="/api/v1/accounts",
    tags=["Accounts"]
)


@router.post(
    "",
    response_model=AccountResponse,
    status_code=status.HTTP_201_CREATED
)
def create_new_account(
    account_data: AccountCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return create_account(
        db,
        current_user.id,
        account_data.account_type
    )


@router.get(
    "",
    response_model=List[AccountResponse]
)
def get_accounts(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return get_user_accounts(
        db,
        current_user.id
    )