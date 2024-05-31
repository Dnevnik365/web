from fastapi import FastAPI

from dnevnik365.api.homeworks import homework_router
from dnevnik365.api.purposes import purposes_router


app = FastAPI()


@app.on_event('startup')
async def on_startup():
    app.include_router(homework_router)
    app.include_router(purposes_router)
