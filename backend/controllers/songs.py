from utils.tokens import get_db_token_spotify
from services import http
from fastapi import HTTPException
import os

env = dict(os.environ)

url_api_spotify = env["URL_API_SPOTIFY"]


async def get_songs(q, limit, token):
    url = url_api_spotify + f"search?q={q}&type=track&limit={limit}"
    headers = {"Authorization": f"Bearer {token}"}
    songs = await http(
        url=url,
        method="get",
        headers=headers,
    )
    return songs


async def get_song(id, token):
    url = url_api_spotify + f"tracks/{id}"
    headers = {"Authorization": f"Bearer {token}"}
    song = await http(url=url, method="get", headers=headers)
    return song
