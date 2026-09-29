import random

from sqlalchemy.orm import Session

from app.models.account import Account


def generate_account_number(db: Session) -> str:
    while True:
        account_number = str(
            random.randint(1000000000, 9999999999)
        )

        existing_account = (
            db.query(Account)
            .filter(
                Account.account_number == account_number
            )
            .first()
        )

        if not existing_account:
            return account_number


def create_account(
    db: Session,
    user_id: int,
    account_type: str
):
    account_number = generate_account_number(db)

    new_account = Account(
        user_id=user_id,
        account_number=account_number,
        account_type=account_type,
        balance=0.00,
        currency="INR",
        status="ACTIVE"
    )

    db.add(new_account)
    db.commit()
    db.refresh(new_account)

    return new_account


def get_user_accounts(
    db: Session,
    user_id: int
):
    return (
        db.query(Account)
        .filter(Account.user_id == user_id)
        .all()
    )