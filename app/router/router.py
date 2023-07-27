from endpoints import account_cash_transactions_api, accounts_api, stocks_api
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(accounts_api.router, prefix="/accounts", tags=["accounts"])
api_router.include_router(
    account_cash_transactions_api.router,
    prefix="/account_cash_transactions",
    tags=["account_cash_transactions"],
)
api_router.include_router(stocks_api.router, prefix="/stocks", tags=["stocks"])
