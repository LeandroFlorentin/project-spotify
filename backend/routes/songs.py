from fastapi import APIRouter
from fastapi.responses import JSONResponse
from controllers.songs import get_songs

router = APIRouter(prefix="/songs")


@router.get("/get_songs")
async def route_songs():
    return JSONResponse(
        content=await get_songs(), status_code=200, media_type="application/json"
    )
