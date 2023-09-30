import uuid
from sqlalchemy import Column, Integer, String
from db import Base, engine


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    login = Column(String(length=20), unique=True, index=True)
    password = Column(String(length=50))
    username = Column(String(length=50), index=True)
    chat_id = Column(String(length=20), unique=True, index=True)


Base.metadata.create_all(bind=engine)
