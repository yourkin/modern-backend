import logging

from fastapi import FastAPI

from ex_back.api.v1.router import router as v1_router
from ex_back.db import create_tables

log = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
    app = FastAPI()
    app.include_router(v1_router, prefix="/v1")
    return app


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    create_tables()


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")