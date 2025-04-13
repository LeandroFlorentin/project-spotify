from services.spotify import get_token_spotify
from utils.tokens import get_db_token_spotify
from models import Token
from datetime import datetime, timedelta
from db import get_session


async def verify_spotify_token():
    session = get_session()
    token_get = get_db_token_spotify("login")
    if len(token_get) == 0:
        token_spotify = await get_token_spotify()
        new_token = Token(
            token=token_spotify["access_token"],
            expires_in=datetime.now() + timedelta(token_spotify["expires_in"]),
        )
        session.add(new_token)
        session.commit()
        session.refresh(new_token)
        token_get = token_spotify["access_token"]
    else:
        expires_str = token_get[0]["expires_in"]
        expires_dt = datetime.fromisoformat(expires_str)
        if expires_dt < datetime.now():
            token_spotify = await get_token_spotify()
            data = {
                "access_token": token_spotify["access_token"],
                "expires_in": datetime.now() + timedelta(token_spotify["expires_in"]),
            }
            token_get[0].sqlmodel_update(data)
            session.add(token_get[0])
            session.commit()
            session.refresh(token_get[0])
            token_get = token_spotify["access_token"]
        else:
            token_get = token_get[0]["access_token"]
    return token_get
