from fastapi import APIRouter

from dnevnik365.models.pydantic import Puproses
from dnevnik365.models.enums import Purpose
from dnevnik365.services.purposes import view, create, remove, on_shutdown, update_one, update_all


purposes_router = APIRouter(prefix='/purposes')


@purposes_router.on_event('shutdown')
async def shutdown():
    return await on_shutdown()


@purposes_router.get('/')
async def view_purposes(user_id: int):
    return await view(user_id)


@purposes_router.post('/')
async def create_purpose(purposes: Puproses):
    return await create(purposes)


@purposes_router.patch('/')
async def update_purpose(user_id: int, subject: str, purpose: Purpose):
    return await update_one(user_id, subject, purpose)


@purposes_router.put('/')
async def update_purposes(purposes: Puproses):
    return await update_all(purposes)


@purposes_router.delete('/')
async def remove_purpose(user_id: int, subject: str):
    return await remove(user_id, subject)
