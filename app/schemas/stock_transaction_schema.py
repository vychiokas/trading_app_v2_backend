from typing import Literal

from pydantic import BaseModel


class StockTransactionCreate(BaseModel):
    action: Literal["buy", "sell"]
    quantity: int
    account_id: int
    ticker: str

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "action": "buy",
                "quantity": 1,
                "account_id": 1,
                "ticker": "BRK.A"
            }
        }


class StockTransactionResponse(BaseModel):
    id: int
    action: Literal["buy", "sell"]
    quantity: int
    account_id: int
    ticker: str

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "quantity": 1,
                "account_id": 1,
                "ticker": "BRK.A"
            }
        }
