from fastapi import APIRouter

from dnevnik365.backend.api.database import purposes as r
from dnevnik365.backend.models.pydantic_models import Puproses, PurposeValue


purposes_router = APIRouter(prefix='/purposes')


@purposes_router.on_event('shutdown')
async def on_shutdown():
    await r.close()


@purposes_router.get('/')
async def view_purposes(user_id: int):
    purposes = await r.hgetall(str(user_id))
    return dict(purposes)


@purposes_router.post('/')
async def create_purpose(purposes: Puproses):
    return r.hmset(str(purposes.user_id), purposes.purposes)


@purposes_router.patch('/')
async def update_purpose(user_id: int, subject: str, purpose: PurposeValue):
    return r.hset(str(user_id), subject, purpose)


@purposes_router.put('/')
async def update_purposes(purposes: Puproses):
    r.hmset(str(purposes.user_id), purposes.purposes)
    return {'status': 'fine'}


@purposes_router.delete('/')
async def remove_purpose(user_id: int, subject: str):
    return r.hdel(user_id, subject)
