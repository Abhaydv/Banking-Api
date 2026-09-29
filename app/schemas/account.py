from pydantic import BaseModel, Field


class AccountCreate(BaseModel):
    account_type: str = Field(
        default="SAVINGS",
        pattern="^(SAVINGS|CURRENT)$"
    )


class AccountResponse(BaseModel):
    id: int
    account_number: str
    account_type: str
    balance: float
    currency: str
    status: str

    class Config:
        from_attributes = True