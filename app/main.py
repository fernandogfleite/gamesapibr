from fastapi import FastAPI
from app.api.router import router
from app.db import (
    engine,
    Base,
    database
)

Base.metadata.create_all(engine)

app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Hello World"}

@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def startup():
    await database.disconnect()

app.include_router(router)