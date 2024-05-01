from fastapi import FastAPI

import logging

from dnevnik365.backend.auth.main import account_router
from dnevnik365.backend.api.purposes import purposes_router
from dnevnik365.backend.api.database import purposes, timetable


logger = logging.getLogger()
app = FastAPI()


@app.on_event('startup')
async def on_startup():
    app.include_router(account_router)
    app.include_router(purposes_router)


@app.on_event('shutdown')
async def on_shutdown():
    await purposes.close()
    await timetable.close()
