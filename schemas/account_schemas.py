from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class AccountCreate(BaseModel):
    name: str
    surname: str
    email: EmailStr
    password: str
    birthdate: datetime
    phone_number: Optional[str]

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Antantas",
                "surname": "Fontanas",
                "email": "antantas123@gmail.com",
                "password": "1234",
                "birthdate": "2023-07-11T18:08:57.215Z",
                "phone_number": "123456"
                }
            }