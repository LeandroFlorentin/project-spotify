from fastapi import APIRouter, responses
from pydantic import BaseModel
from typing import List
from controllers.users import create_user, get_user
from utils.bearer_token import get_bearer_token

router = APIRouter(prefix="/users")


class BodyCreate(BaseModel):
    username: str
    email: str
    password: str
    role: list[str]


class UserData(BaseModel):
    id: int
    username: str
    email: str
    role: List[str]
    disabled: int
    access_token: str


class Response_create(BaseModel):
    status: int
    message: str
    data: UserData


class Data_get(BaseModel):
    id: int
    username: str
    email: str
    role: List[str]
    createdAt: str
    updatedAt: str


class Response_get(BaseModel):
    status: int
    message: str
    data: Data_get


@router.get("/me")
async def route_me(id: int, token: str = get_bearer_token()) -> Response_get:
    return responses.JSONResponse(
        content=await get_user(id, token),
        status_code=200,
        media_type="application/json",
    )


@router.post("/create")
async def route_create(
    body: BodyCreate, token: str = get_bearer_token()
) -> Response_create:
    body_dict = body.model_dump()
    return responses.JSONResponse(
        content=await create_user(body_dict, token),
        status_code=200,
        media_type="application/json",
    )
