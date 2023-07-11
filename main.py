from typing import List

from fastapi import FastAPI

from schemas.account_schemas import AccountCreate
app = FastAPI()


@app.post("/users/", response_model=AccountCreate)
def create_user(account: AccountCreate):
    return account.model_dump()


@app.get("/users/", response_model=List[AccountCreate])
def get_all_users():
    return [AccountCreate.Config.json_schema_extra["example"]]

