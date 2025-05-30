from fastapi import APIRouter, Depends, responses
from controllers.favourites import add_favourite, get_favourites, delete_favourite
from middlewares.jwt import decode_token_dependency
from types_routes.favourites import Body_add_favourite
from utils.swagger import show_bearer_in_swagger

router = APIRouter(prefix="/favourites", tags=["Favourites"])


@router.post(
    "/add", dependencies=[Depends(show_bearer_in_swagger)], summary="Add favourite"
)
async def add_favourite_route(
    body: Body_add_favourite,
    user_data=Depends(decode_token_dependency),
):
    body_dict = body.model_dump()
    result = await add_favourite(body_dict, user_data)
    return responses.JSONResponse(
        content=result,
        status_code=result["status"],
        media_type="application/json",
    )


@router.get("/get", dependencies=[Depends(show_bearer_in_swagger)])
async def get_favourites_route(user_data=Depends(decode_token_dependency)):
    result = await get_favourites(user_data["id"])
    return responses.JSONResponse(
        content=result,
        status_code=result["status"],
        media_type="application/json",
    )


@router.delete(f"/delete", dependencies=[Depends(show_bearer_in_swagger)])
async def delete_favourite_route(id: int, user_data=Depends(decode_token_dependency)):
    result = await delete_favourite(id)
    return responses.JSONResponse(
        content=result,
        status_code=result["status"],
        media_type="application/json",
    )
