from fastapi import APIRouter
from . import songs, auth, users, favourites

router_modules = [songs, auth, users, favourites]

main_router = APIRouter()
for router_module in router_modules:
    main_router.include_router(router_module.router)
