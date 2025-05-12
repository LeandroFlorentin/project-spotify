from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from controllers.songs import get_songs, get_song, get_songs_via_url
from utils.swagger import show_bearer_in_swagger
from middlewares.jwt import decode_token_dependency
from middlewares.spotify_token import verify_spotify_token

router = APIRouter(prefix="/songs", tags=["Songs"])


@router.get(
    "/get_songs",
    dependencies=[Depends(show_bearer_in_swagger)],
    summary="Get songs",
    description="Get songs from API Spotify",
)
async def route_songs(
    q: str,
    limit: int = 10,
    token_spotify=Depends(verify_spotify_token),
    token_data=Depends(decode_token_dependency),
):
    result = await get_songs(q, limit, token_spotify)
    return JSONResponse(
        content=result,
        status_code=result.get("status", 200),
        media_type="application/json",
    )


@router.get(
    "/get_song",
    dependencies=[Depends(show_bearer_in_swagger)],
    summary="Get song",
    description="Get song by id from API spotify",
)
async def router_song(
    id: str,
    token_spotify=Depends(verify_spotify_token),
    token_data=Depends(decode_token_dependency),
):
    result = await get_song(id, token_spotify)
    return JSONResponse(
        content=result,
        status_code=result.get("status", 200),
        media_type="application/json",
    )


@router.get(
    "/get_songs_via_url",
    dependencies=[Depends(show_bearer_in_swagger)],
    summary="Get song",
    description="Get song by id from API spotify",
)
async def router_song_via_url(
    url_songs: str,
    token_spotify=Depends(verify_spotify_token),
    token_data=Depends(decode_token_dependency),
):
    result = await get_songs_via_url(url_songs, token_spotify)
    return JSONResponse(
        content=result,
        status_code=result.get("status", 200),
        media_type="application/json",
    )
