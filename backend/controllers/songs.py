from utils.tokens import get_db_token_spotify
from services import http
from fastapi import HTTPException
import os

env = dict(os.environ)


async def get_songs(q, type, limit):
    query = f"?q={q}&type={type}&limit={limit}"
    token_db_spotify = get_db_token_spotify("routes")
    token_spotify = token_db_spotify[0]["token"]
    headers = {"Authorization": f"Bearer {token_spotify}"}
    songs = await http(
        env["URL_API_SPOTIFY"] + f"search{query}",
        method="get",
        headers=headers,
    )
    return songs
