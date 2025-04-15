from fastapi import APIRouter, responses, HTTPException
from controllers.auth import login
from middlewares.spotify_token import verify_spotify_token
from types_routes.auth import BodyLogin, Response

json_response = responses.JSONResponse

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post(
    "/login",
)
async def auth_route(body: BodyLogin) -> Response:
    try:
        body_dic = body.model_dump()
        result = await login(body_dic)

        if not result:
            raise HTTPException(status_code=401, detail="Credenciales inválidas")

        return json_response(
            content=result,
            status_code=200,
            media_type="application/json",
        )
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error en la autenticación: {str(e)}"
        )
