from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from controllers.songs import get_songs, get_song
from utils.swagger import show_bearer_in_swagger
from middlewares.jwt import decode_token_dependency
from middlewares.spotify_token import verify_spotify_token

router = APIRouter(prefix="/songs")


@router.get(
    "/get_songs",
    dependencies=[Depends(show_bearer_in_swagger)],
)
async def route_songs(
    q: str,
    limit: int = 10,
    token_spotify=Depends(verify_spotify_token),
    token_data=Depends(decode_token_dependency),
):
    return JSONResponse(
        content=await get_songs(q, limit, token_spotify),
        status_code=200,
        media_type="application/json",
    )


@router.get("/get_song", dependencies=[Depends(show_bearer_in_swagger)])
async def router_song(
    id: str,
    token_spotify=Depends(verify_spotify_token),
    token_data=Depends(decode_token_dependency),
):
    return JSONResponse(
        content=await get_song(id, token_spotify),
        status_code=200,
        media_type="application/json",
    )
