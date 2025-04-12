from services import http, get_token_spotify
from models.token import Token
from datetime import datetime, timedelta
from db import get_session
from fastapi import HTTPException
from sqlalchemy import select
from utils.jwt import decoded_token
import os

env = dict(os.environ)


async def login(body):
    try:
        session = get_session()
        response = await http(
            url=env["URL_MICROSERVICE_AUTH"] + "auth/login",
            method="post",
            body=body,
            params=None,
            headers=None,
            data=None,
        )
        token_get = session.exec(select(Token)).scalars().all()
        if len(token_get) == 0:
            token_spotify = await get_token_spotify()
            new_token = Token(
                token=token_spotify["access_token"],
                expires_in=datetime.now() + timedelta(token_spotify["expires_in"]),
            )
            session.add(new_token)
            session.commit()
            session.refresh(new_token)
        else:
            if token_get[0].expires_in < datetime.now():
                token_spotify = await get_token_spotify()
                data = {
                    "access_token": token_spotify["access_token"],
                    "expires_in": datetime.now()
                    + timedelta(token_spotify["expires_in"]),
                }
                token_get[0].sqlmodel_update(data)
                session.add(token_get[0])
                session.commit()
                session.refresh(token_get[0])
        return response
    except HTTPException as err:
        raise HTTPException(
            status_code=err.response.status_code, detail=err.response.text
        )
