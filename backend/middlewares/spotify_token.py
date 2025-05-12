from services.spotify import get_token_spotify
from utils.tokens import get_db_token_spotify
from models import Token
from datetime import datetime, timedelta
from db import get_session


async def verify_spotify_token():
    session = get_session()
    token_get = get_db_token_spotify("login", session)
    if len(token_get) == 0:
        token_spotify = await get_token_spotify()
        print("TUKEN", token_spotify)
        new_token = Token(
            token=token_spotify["access_token"],
            expires_in=datetime.now() + timedelta(seconds=token_spotify["expires_in"]),
        )
        session.add(new_token)
        session.commit()
        session.refresh(new_token)
        token_get = token_spotify["access_token"]
    else:
        expires_dt = token_get[0].expires_in
        if expires_dt < datetime.now():
            token_spotify = await get_token_spotify()
            data = {
                "token": token_spotify["access_token"],
                "expires_in": datetime.now()
                + timedelta(seconds=token_spotify["expires_in"]),
            }
            token_get[0].sqlmodel_update(data)
            session.add(token_get[0])
            session.commit()
            session.refresh(token_get[0])
            token_get = token_spotify["access_token"]
        else:
            token_get = token_get[0].token
    return token_get
