from pydantic import BaseModel


class StockResponce(BaseModel):
    price: float
