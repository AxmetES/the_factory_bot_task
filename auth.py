import time
import jwt
from decouple import config

JWT_SECRET = config("SECRET_KEY")
ALGORITHM = config("ALGORITHM")


def token_response(token: str):
    return token


def signJWT(userID: str):
    payload = {
        "userID": userID,
        "expiry": int(time.time() + 20000),
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=ALGORITHM)
    return token_response(token)


def decodeJWT(token: str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithms=ALGORITHM)
        return decode_token if decode_token['expiry'] >= time.time() else None
    except:
        return {}