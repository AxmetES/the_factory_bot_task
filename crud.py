import logging

import models
import schemas
from db import SessionLocal, get_db, get_session


def get_or_create_user(body: schemas.UserSchema):
    with get_session() as db:
        user = db.query(models.User).filter(models.User.username == body.username).first()
        if user:
            return user.token
        else:
            try:
                new_user = models.User(login=body.login,
                                       password=body.password,
                                       username=body.username)
                db.add(new_user)
            except Exception as e:
                db.rollback()
                logging.exception(e)


def add_chat_to_user(login, chat_id):
    with get_session() as db:
        user = db.query(models.User).filter(models.User.login == login).first()
        if user:
            user.chat_id = chat_id
            return True
        return False


def add_token(user, token):
    with get_session() as db:
        user = db.query(models.User).filter(models.User.login == user.login,
                                            models.User.username == user.username).first()
        user.token = token
