from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from typing import Optional, List

from models.account_cash_transactions import AccountCashTransaction
import schemas.account_cash_transaction_schemas
from crud.account_crud import get_account


def create_transaction(
    db: Session,
    account_id,
    account_cash_transaction: schemas.account_cash_transaction_schemas.AccountCashTransactionCreate,
) -> Optional[AccountCashTransaction]:
    db_account = get_account(db, account_id)
    if db_account:
        db_account_cash_transaction = AccountCashTransaction(
            amount=account_cash_transaction.amount,
            creation_date=account_cash_transaction.creation_date,
            status=account_cash_transaction.status,
        )

        db_account.transactions.append(db_account_cash_transaction)
        db.add(db_account_cash_transaction)
        db.commit()
        db.refresh(db_account_cash_transaction)
        return db_account_cash_transaction
    else:
        raise NoResultFound


def get_transactions(db: Session, account_id: int) -> List[AccountCashTransaction]:
    return (
        db.query(AccountCashTransaction)
        .filter(AccountCashTransaction.account_id == account_id)
        .all()
    )


def get_balance(db: Session, account_id: int) -> float:
    balance = 0
    cash_transactions = (
        db.query(AccountCashTransaction).filter(account_id == account_id).all()
    )
    for transaction in cash_transactions:
        balance += transaction.amount
    return balance
