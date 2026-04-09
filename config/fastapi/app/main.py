from fastapi import FastAPI

from app.routers.static_endpoint import router
from app.routers.dynamic_content import router_dynamic_users_from_db

app = FastAPI()

app.include_router(router, prefix="/app")
app.include_router(router_dynamic_users_from_db, prefix="/app")
