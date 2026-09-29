from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database.database import Base


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    account_number = Column(
        String(20),
        unique=True,
        index=True,
        nullable=False
    )

    account_type = Column(
        String(20),
        default="SAVINGS",
        nullable=False
    )

    balance = Column(
        Numeric(12, 2),
        default=0.00,
        nullable=False
    )

    currency = Column(
        String(3),
        default="INR",
        nullable=False
    )

    status = Column(
        String(20),
        default="ACTIVE",
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    user = relationship(
        "User",
        back_populates="accounts"
    )

    transactions = relationship(
        "Transaction",
        back_populates="account",
        cascade="all, delete-orphan"
    )