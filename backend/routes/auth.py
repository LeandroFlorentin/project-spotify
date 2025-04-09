from fastapi import APIRouter, responses
from pydantic import BaseModel
from controllers.auth import login
import json

json_response = responses.JSONResponse

router = APIRouter(prefix="/auth")


class BodyLogin(BaseModel):
    username: str
    password: str


@router.post("/login")
async def auth_route(body: BodyLogin):
    body_dic = body.model_dump()
    body_json = json.dumps(body_dic)
    return json_response(
        content=await login(body_json), status_code=200, media_type="application/json"
    )
