from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from sqlalchemy.orm.exc import NoResultFound
from database.db import get_db
import crud.account_cash_transactions_crud, crud.account_crud
from schemas.account_cash_transaction_schemas import (
    AccountCashTransactionCreate,
    AccountCashTransactionResponse,
    BalanceResponse,
)


router = APIRouter()


@router.get("/{account_id}", response_model=List[AccountCashTransactionResponse])
def get_transactions(account_id: int, db: Session = Depends(get_db)):
    db_account = crud.account_crud.get_account(db, account_id)
    if db_account:
        transactions = crud.account_cash_transactions_crud.get_transactions(
            db, account_id
        )
        return transactions
    else:
        raise HTTPException(status_code=404, detail=f"Account {account_id} not found")


@router.post("/{account_id}", response_model=AccountCashTransactionResponse)
def create_transaction(
    account_id: int,
    account_cash_transaction: AccountCashTransactionCreate,
    db: Session = Depends(get_db),
):
    db_account = crud.account_crud.get_account(db, account_id)
    if db_account:
        return crud.account_cash_transactions_crud.create_transaction(
            db, account_id, account_cash_transaction
        )
    else:
        HTTPException(status_code=404, detail=f"Account {account_id} not found")


@router.get("/{account_id}/balance", response_model=BalanceResponse)
def get_balance(account_id: int, db: Session = Depends(get_db)):
    db_account = crud.account_crud.get_account(db, account_id)
    if db_account:
        amount = crud.account_cash_transactions_crud.get_balance(db, account_id)
        return {"balance": amount}
    else:
        raise HTTPException(status_code=404, detail=f"Account {account_id} not found")
