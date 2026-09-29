import uuid
from decimal import Decimal

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.account import Account
from app.models.transaction import Transaction


def generate_reference() -> str:
    return f"TXN-{uuid.uuid4().hex[:12].upper()}"


def deposit(
    db: Session,
    account: Account,
    amount: float
):
    if account.status != "ACTIVE":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Account is not active"
        )

    amount = Decimal(str(amount))

    account.balance += amount

    transaction = Transaction(
        account_id=account.id,
        transaction_type="DEPOSIT",
        amount=amount,
        reference=generate_reference(),
        description="Cash deposit"
    )

    db.add(transaction)

    try:
        db.commit()
        db.refresh(account)
        db.refresh(transaction)
    except Exception:
        db.rollback()
        raise

    return transaction


def withdraw(
    db: Session,
    account: Account,
    amount: float
):
    if account.status != "ACTIVE":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Account is not active"
        )

    amount = Decimal(str(amount))

    if account.balance < amount:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Insufficient balance"
        )

    account.balance -= amount

    transaction = Transaction(
        account_id=account.id,
        transaction_type="WITHDRAW",
        amount=amount,
        reference=generate_reference(),
        description="Cash withdrawal"
    )

    db.add(transaction)

    try:
        db.commit()
        db.refresh(account)
        db.refresh(transaction)
    except Exception:
        db.rollback()
        raise

    return transaction


def transfer(
    db: Session,
    from_account: Account,
    to_account: Account,
    amount: float
):
    if from_account.status != "ACTIVE":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Source account is not active"
        )

    if to_account.status != "ACTIVE":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Destination account is not active"
        )

    if from_account.id == to_account.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot transfer to the same account"
        )

    amount = Decimal(str(amount))

    if from_account.balance < amount:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Insufficient balance"
        )

    from_account.balance -= amount
    to_account.balance += amount

    transfer_reference = generate_reference()

    sender_transaction = Transaction(
        account_id=from_account.id,
        transaction_type="TRANSFER_OUT",
        amount=amount,
        reference=transfer_reference,
        description=f"Transfer to account {to_account.account_number}"
    )

    receiver_transaction = Transaction(
        account_id=to_account.id,
        transaction_type="TRANSFER_IN",
        amount=amount,
        reference=generate_reference(),
        description=f"Transfer from account {from_account.account_number}"
    )

    db.add(sender_transaction)
    db.add(receiver_transaction)

    try:
        db.commit()
        db.refresh(sender_transaction)
    except Exception:
        db.rollback()
        raise

    return sender_transaction


def get_transactions(
    db: Session,
    account_id: int
):
    return (
        db.query(Transaction)
        .filter(
            Transaction.account_id == account_id
        )
        .order_by(
            Transaction.created_at.desc()
        )
        .all()
    )