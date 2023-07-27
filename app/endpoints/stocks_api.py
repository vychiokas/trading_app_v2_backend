from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
import crud.stocks_crud

from schemas.stocks_schemas import StockResponce

router = APIRouter()


@router.get("/{ticker}", response_model=StockResponce)
def get_price(ticker: str):
    ticker_price = crud.stocks_crud.get_price(ticker)
    return {"price": ticker_price}
