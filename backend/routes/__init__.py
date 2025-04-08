from fastapi import APIRouter
from . import songs

router_modules = [songs]

main_router = APIRouter()
for router_module in router_modules:
    main_router.include_router(router_module.router)
