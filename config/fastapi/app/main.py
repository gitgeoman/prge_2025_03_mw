from fastapi import FastAPI

from app.routers.static_endpoint import router
from app.routers.dynamic_content import router_dynamic_users_from_db
from app.routers.db_insert import router_db_insert

app = FastAPI()

app.include_router(router, prefix="/app")
app.include_router(router_dynamic_users_from_db, prefix="/app")
app.include_router(router_db_insert, prefix="/app")