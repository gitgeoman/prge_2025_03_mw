from fastapi import FastAPI

from app.routers.static_endpoint import router

app = FastAPI()

app.include_router(router, prefix="/app")
