from fastapi import APIRouter
from fastapi.responses import JSONResponse
from controllers.songs import get_songs

router = APIRouter()


@router.get("/songs/get_songs")
def route_songs():
    return JSONResponse(
        content=get_songs(), status_code=200, media_type="application/json"
    )
