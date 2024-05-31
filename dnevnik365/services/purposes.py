from dnevnik365.core.database import purposes as r
from dnevnik365.models.pydantic import Puproses
from dnevnik365.models.enums import Purpose


async def on_shutdown():
    await r.close()


async def view(user_id: int):
    purposes = await r.hgetall(str(user_id))
    return dict(purposes)


async def create(purposes: Puproses):
    return r.hmset(str(purposes.user_id), purposes.purposes)


async def update_one(user_id: int, subject: str, purpose: Purpose):
    return r.hset(str(user_id), subject, purpose)


async def update_all(purposes: Puproses):
    r.hmset(str(purposes.user_id), purposes.purposes)
    return {'status': 'fine'}


async def remove(user_id: int, subject: str):
    return r.hdel(user_id, subject)
