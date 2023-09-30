from pydantic import BaseModel


class UserSchema(BaseModel):
    login: str
    password: str
    username: str


class UserLogin(BaseModel):
    login: str
    password: str
