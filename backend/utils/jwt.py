import jwt
import os

env = dict(os.environ)


def decoded_token(token: str):
    return jwt.decode(token, env["JWT_SECRET"], algorithms=["HS256"])
