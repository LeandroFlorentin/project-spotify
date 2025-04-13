from fastapi import Request, HTTPException
from db import get_session
from sqlalchemy import select
from models.token import Token


def get_bearer_token(request: Request):
    token = request.headers.get("authorization")

    if not token or not token.startswith("Bearer "):
        raise HTTPException(400, "Token not found")

    return token


def get_db_token_spotify(call="routes"):
    session = get_session()
    get_tokens_spotify = session.exec(select(Token)).scalars().all()
    if call != "login":
        if len(get_tokens_spotify) == 0:
            raise HTTPException(404, "No spotify tokens found in database")
    token_list = [
        {
            "id": t.id,
            "token": t.token,
            "expires_in": t.expires_in.isoformat() if t.expires_in else None,
        }
        for t in get_tokens_spotify
    ]

    return token_list
