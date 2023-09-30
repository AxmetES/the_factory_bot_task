import models
from db import get_session
from schemas import UserLogin


def check_user(data: UserLogin, db):
    user = db.query(models.User).filter(
        models.User.login == data.login,
        models.User.password == data.password
    ).first()
    if user:
        return True
    return False


def get_chat_id(login):
    with get_session() as db:
        user = db.query(models.User).filter(models.User.login == login).first()
        if user:
            return user.chat_id
