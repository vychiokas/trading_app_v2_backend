from datetime import datetime
from typing import Literal

from pydantic import BaseModel


class AccountCashTransactionCreate(BaseModel):
    amount: float
    creation_date: datetime
    status: Literal["TOP-UP", "BUYING-SHARES", "SELLING-SHARES", "WITHDRAWAL"]

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "amount": 101.1,
                "creation_date": "2023-07-11T18:08:57.215Z",
                "status": "TOP-UP",
            }
        }


class AccountCashTransactionResponse(BaseModel):
    id: int
    amount: float
    creation_date: datetime
    status: Literal["TOP-UP", "BUYING-SHARES", "SELLING-SHARES", "WITHDRAWAL"]

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "amount": 101.1,
                "creation_date": "2023-07-11T18:08:57.215Z",
                "status": "TOP-UP",
            }
        }


class BalanceResponse(BaseModel):
    balance: float
