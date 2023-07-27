from stocks_price import get_stock_price
from sqlalchemy.orm.exc import NoResultFound


def get_price(ticker: str) -> float:
    price = get_stock_price(ticker)
    if price > 0:
        return price
    else:
        return NoResultFound
