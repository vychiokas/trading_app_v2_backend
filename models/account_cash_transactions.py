import enum

from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey, Numeric, Enum
from sqlalchemy.orm import relationship

from database.db import Base


class MyEnum(enum.Enum):
    TOP_UP = 1
    BUYING_SHARES = 2
    SELLING_SHARES = 3
    WITHDRAWAL = 4


class AccountCashTransaction(Base):
    __tablename__ = "account_cash_transactions"

    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey("accounts.id"))
    amount = Column(Numeric(10, 2))
    creation_date = Column(DateTime)
    status = Column(Enum(MyEnum))
    password = Column(String)
    
    account = relationship("Account", back_populates="transactions")
