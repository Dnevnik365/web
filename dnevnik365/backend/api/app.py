from fastapi import FastAPI, Form
from fastapi.exceptions import HTTPException

from sqlalchemy.orm import sessionmaker

import logging

from dnevnik365.backend.auth.main import User, account_router
from dnevnik365.backend.api.purposes import purposes_router
from dnevnik365.backend.api.database import engine
from dnevnik365.backend.models.models import metadata
from dnevnik365.backend.scripts import dnevnikru, ballovnet, eljur, kirov_education


logger = logging.getLogger()
app = FastAPI()


@app.on_event('startup')
async def on_startup():
    app.include_router(account_router)
    metadata.create_all(engine)


@app.on_event('shutdown')
async def on_shutdown():
    metadata.drop_all(engine)
