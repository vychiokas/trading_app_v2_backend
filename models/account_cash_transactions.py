from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship

from database.db import Base


class AccountCashTransaction(Base):
    __tablename__ = "account_cash_transaction"
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    creation_date = Column(DateTime)
    status = Column(String)
    account_id = Column(Integer, ForeignKey("accounts.id"))
    account = relationship("Account")
