from database.db import Base
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class StockTransaction(Base):
    __tablename__ = "stock_transactions"
    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String)
    action = Column(String)
    creation_date = Column(DateTime(timezone=True), server_default=func.now())
    quantity = Column(Integer)
    stock_price = Column(Float)
    account_id = Column(Integer, ForeignKey("accounts.id"))
    account_cash_transaction_id = Column(Integer, ForeignKey("account_cash_transaction.id"))
    
    account = relationship("Account")
    account_cash_transaction = relationship("AccountCashTransaction")
