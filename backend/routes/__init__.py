from fastapi import APIRouter
from . import songs, auth

router_modules = [songs, auth]

main_router = APIRouter()
for router_module in router_modules:
    main_router.include_router(router_module.router)
