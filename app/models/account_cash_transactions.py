from database.db import Base
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class AccountCashTransaction(Base):
    __tablename__ = "account_cash_transaction"
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    creation_date = Column(DateTime(timezone=True), server_default=func.now())
    status = Column(String)
    account_id = Column(Integer, ForeignKey("accounts.id"))
    account = relationship("Account")
