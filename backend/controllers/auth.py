from services import http, get_token_spotify
from models.token import Token
from db import get_session
from fastapi import HTTPException
import os

env = dict(os.environ)


async def login(body):
    try:
        response = await http(
            url=env["URL_MICROSERVICE_AUTH"] + "auth/login",
            method="post",
            body=body,
            params=None,
            headers=None,
            data=None,
        )
        return response
    except HTTPException as err:
        raise HTTPException(
            status_code=err.response.status_code, detail=err.response.text
        )
