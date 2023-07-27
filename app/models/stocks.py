from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float


class StockTransactions(Base):
    __tablename__ = "stock_transactions"
    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String)
    action = Column(String)
    time = Column(DateTime)
    quantity = Column(Integer)
    stock_price = Column(Float)
    account_id = Column(Integer, ForeignKey="account.id")
