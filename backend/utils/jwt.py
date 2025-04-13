from fastapi import HTTPException
import jwt
import os

env = dict(os.environ)


def decoded_token(token: str):
    try:
        return jwt.decode(token, env["JWT_SECRET"], algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise HTTPException(401, "Expired token")
    except jwt.InvalidTokenError:
        raise HTTPException(401, "Invalid token")
