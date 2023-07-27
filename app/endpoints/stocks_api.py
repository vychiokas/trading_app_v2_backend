import crud.stocks_crud
from database.db import get_db
from fastapi import APIRouter, Depends, HTTPException
from schemas.stock_transaction_schema import (StockTransactionCreate,
                                              StockTransactionResponse)
from schemas.stocks_schemas import StockResponce
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

router = APIRouter()


@router.get("/{ticker}", response_model=StockResponce)
def get_price(ticker: str):
    ticker_price = crud.stocks_crud.get_price(ticker)
    return {"price": ticker_price}


@router.post("", response_model=StockTransactionResponse)
def register_stock_purchase(new_stock_transaction: StockTransactionCreate, db: Session = Depends(get_db)):
    stock_transaction = crud.stocks_crud.register_user_buying_share(db, new_stock_transaction)
    return stock_transaction