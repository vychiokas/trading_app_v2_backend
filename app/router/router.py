from fastapi import APIRouter

from endpoints import accounts_api, account_cash_transactions_api


api_router = APIRouter()

api_router.include_router(accounts_api.router, prefix="/accounts", tags=["accounts"])
api_router.include_router(
    account_cash_transactions_api.router,
    prefix="/account_cash_transactions",
    tags=["account_cash_transactions"],
)
