from fastapi import APIRouter, responses
from pydantic import BaseModel
from controllers.auth import login
from typing import Dict

json_response = responses.JSONResponse

router = APIRouter(prefix="/auth")


class BodyLogin(BaseModel):
    username: str
    password: str


class Data(BaseModel):
    id: int
    username: str
    email: str
    role: str
    access_token: str


class Response(BaseModel):
    status: int
    message: str
    data: Data


@router.post("/login")
async def auth_route(body: BodyLogin) -> Response:
    body_dic = body.model_dump()
    return json_response(
        content=await login(body_dic), status_code=200, media_type="application/json"
    )
