from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from controllers.songs import get_songs
from utils.swagger import show_bearer_in_swagger
from middlewares.jwt import decode_token_dependency

router = APIRouter(prefix="/songs")


@router.get(
    "/get_songs",
    dependencies=[Depends(show_bearer_in_swagger)],
)
async def route_songs(
    q: str, type: str, limit: int = 10, token_data=Depends(decode_token_dependency)
):
    return JSONResponse(
        content=await get_songs(q, type, limit),
        status_code=200,
        media_type="application/json",
    )
