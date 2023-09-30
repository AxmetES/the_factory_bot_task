from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from auth import decodeJWT


class JwtBearer(HTTPBearer):
    def __init__(self, auto_Error: bool = True):
        super(JwtBearer, self).__init__(auto_error=auto_Error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(
            JwtBearer,
            self
        ).__call__(request)
        if credentials:
            if not credentials.scheme == 'Bearer':
                raise HTTPException(status_code=403, detail="Invalid or expired token")
            request.state.jwt_token = credentials.credentials
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid or expired token")

    def verify_jwt(self, jwt_token: str):
        isTokenValid: bool = False
        payload = decodeJWT(jwt_token)
        if payload:
            isTokenValid = True
        return isTokenValid

