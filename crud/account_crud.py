from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

from models.account import Account
import schemas.account_schemas


def get_account(db: Session, account_id: int):
    return db.query(Account).filter(Account.id == account_id).first()


def get_account_by_email(db: Session, email: str):
    return db.query(Account).filter(Account.email == email).first()


def get_accounts(db: Session):
    return db.query(Account).all()


def create_account(db: Session, account: schemas.account_schemas.AccountCreate):
    fake_hashed_password = account.password + "notreallyhashed"
    db_account = Account(name=account.name,
                         surname=account.surname,
                         email=account.email,
                         password=fake_hashed_password,
                         birthdate=account.birthdate,
                         phone_number=account.phone_number
                         )
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account


def delete_account(db: Session, account_id: int):
    account = get_account(db, account_id)
    if account:
        db.delete(account)
        db.commit()
        return account
    else:
        raise NoResultFound


def update_account():
    pass