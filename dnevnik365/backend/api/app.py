from fastapi import FastAPI

import logging

from dnevnik365.backend.api.homeworks import homework_router
from dnevnik365.backend.api.purposes import purposes_router


logger = logging.getLogger()
app = FastAPI()


@app.on_event('startup')
async def on_startup():
    app.include_router(homework_router)
    app.include_router(purposes_router)
