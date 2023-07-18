from fastapi import Depends, FastAPI


from router.router import api_router

from database.base import Base
from database.db import engine


Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(api_router, prefix="/api/v1")
