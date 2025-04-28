from fastapi import APIRouter, responses, Depends, Request
from controllers.users import create_user, get_user, update_user, delete_user
from utils.tokens import get_bearer_token
from types_routes.users import Response_get, Response_create, Generic_response, BodyUser
from utils.swagger import show_bearer_in_swagger

router = APIRouter(prefix="/users", tags=["Users"])


@router.get(
    "/me", dependencies=[Depends(show_bearer_in_swagger)], summary="Get my user"
)
async def route_me(id: int, request: Request) -> Response_get:
    token = get_bearer_token(request=request)
    return responses.JSONResponse(
        content=await get_user(id, token),
        status_code=200,
        media_type="application/json",
    )


@router.post(
    "/create", dependencies=[Depends(show_bearer_in_swagger)], summary="Create user"
)
async def route_create(body: BodyUser, request: Request) -> Response_create:
    token = get_bearer_token(request=request)
    body_dict = body.model_dump()
    result = await create_user(body_dict, token)
    return responses.JSONResponse(
        content=result,
        status_code=result["status"],
        media_type="application/json",
    )


@router.put(
    "/update", dependencies=[Depends(show_bearer_in_swagger)], summary="Update user"
)
async def route_update(body: BodyUser, request: Request) -> Generic_response:
    token = get_bearer_token(request=request)
    body_dict = body.model_dump()
    result = await update_user(body_dict, id, token)
    return responses.JSONResponse(
        content=result,
        status_code=result["status"],
        media_type="application/json",
    )


@router.delete(
    "/delete", dependencies=[Depends(show_bearer_in_swagger)], summary="Delete user"
)
async def route_delete(id: int, request: Request) -> Generic_response:
    token = get_bearer_token(request=request)
    result = await delete_user(id, token)
    return responses.JSONResponse(
        content=result,
        status_code=result["status"],
        media_type="aplication/json",
    )
