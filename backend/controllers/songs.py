from services import http
from typing import Dict, Union
import os
import math

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
    new_format_songs = change_format_songs(songs)
    format_with_pages = calculate_pagination(new_format_songs)
    return format_with_pages


async def get_song(id, token):
    url = url_api_spotify + f"tracks/{id}"
    headers = {"Authorization": f"Bearer {token}"}
    song = await http(url=url, method="get", headers=headers)
    return song


async def get_songs_via_url(url_songs, token):
    headers = {"Authorization": f"Bearer {token}"}
    songs = await http(
        url=url_songs,
        method="get",
        headers=headers,
    )
    new_format_songs = change_format_songs(songs)
    format_with_pages = calculate_pagination(new_format_songs)
    return format_with_pages


def calculate_pagination(songs) -> Dict[str, int]:
    items = songs["tracks"]
    items["total_pages"] = math.ceil(items["total"] / items["limit"])
    items["page"] = (items["offset"] // items["limit"]) + 1
    for key in ["limit", "offset", "total"]:
        del items[key]
    return {"tracks": items}


def change_format_songs(songs):
    new_format_songs = []
    for song in songs["tracks"]["items"]:
        new_format_songs.append(
            {
                "idspotify": song["id"],
                "title": song["name"],
                "artist": song["artists"],
                "album": song["album"],
                "duration": round(song["duration_ms"] / 1000 / 60, 2),
            }
        )
    songs["tracks"]["items"] = new_format_songs
    return songs
