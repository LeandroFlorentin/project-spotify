from fastapi import APIRouter, responses
from controllers.auth import login
from middlewares.spotify_token import verify_spotify_token
from types_routes.auth import BodyLogin, Response

json_response = responses.JSONResponse

router = APIRouter(prefix="/auth")


@router.post("/login")
async def auth_route(body: BodyLogin) -> Response:
    body_dic = body.model_dump()
    return json_response(
        content=await login(body_dic),
        status_code=200,
        media_type="application/json",
    )
