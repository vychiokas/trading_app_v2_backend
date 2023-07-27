from crud.account_cash_transactions_crud import get_balance
from crud.account_crud import get_account
from models.account_cash_transactions import AccountCashTransaction
from models.stock_transactions import StockTransaction
from schemas.stock_transaction_schema import StockTransactionCreate
                                            
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from stocks_price import get_stock_price


def get_price(ticker: str) -> float:
    price = get_stock_price(ticker)
    if price > 0:
        return price
    else:
        return NoResultFound


def register_user_buying_share(db: Session, new_stock_transaction: StockTransactionCreate) -> StockTransaction:
    if account := get_account(db, new_stock_transaction.account_id):
        account_balance = get_balance(db, account.id)
        stock_price = get_price(new_stock_transaction.ticker)
        required_cash_for_transaction = stock_price * new_stock_transaction.quantity
        if account_balance >= required_cash_for_transaction:
            cash_transaction = AccountCashTransaction(amount=required_cash_for_transaction,
                                                      status="BUYING-SHARES",
                                                      account_id=account.id                                                      
                                                      )
            stock_transaction = StockTransaction(ticker=new_stock_transaction.ticker,
                                                 action="buy",
                                                 quantity=new_stock_transaction.quantity,
                                                 stock_price=stock_price,
                                                 account_id=account.id)
            stock_transaction.account_cash_transaction = cash_transaction
            db.add(stock_transaction)
            db.commit()
            return stock_transaction
            