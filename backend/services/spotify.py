from services import http
from fastapi import HTTPException
import os

env = dict(os.environ)


async def get_token_spotify():
    client_id = env["CLIENT_ID"]
    client_secret = env["CLIENT_SECRET"]
    url_spotify = env["URL_SPOTIFY"]
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
    }
    try:
        response = await http(
            url=url_spotify + "api/token",
            method="post",
            body=None,
            params=None,
            headers=headers,
            data=data,
        )
        return response
    except HTTPException as err:
        raise HTTPException(
            status_code=err.response.status_code, detail=err.response.text
        )
