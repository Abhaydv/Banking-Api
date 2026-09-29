from pydantic import BaseModel, Field


class DepositRequest(BaseModel):
    amount: float = Field(..., gt=0)


class WithdrawRequest(BaseModel):
    amount: float = Field(..., gt=0)


class TransferRequest(BaseModel):
    to_account_id: int
    amount: float = Field(..., gt=0)


class TransactionResponse(BaseModel):
    id: int
    account_id: int
    transaction_type: str
    amount: float
    reference: str
    description: str | None
    created_at: object

    class Config:
        from_attributes = True