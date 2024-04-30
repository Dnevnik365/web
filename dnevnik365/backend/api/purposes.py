from fastapi import APIRouter

from dnevnik365.backend.api.database import purposes
from dnevnik365.backend.models.models import Puproses


purposes_router = APIRouter(prefix='/puroses')


@purposes_router.get('/{subject}')
async def view_purposes(subject: str = None):
    if subject is None:
        return  # all subjects


@purposes_router.get('/new')
async def get_create_purpose():
    return


@purposes_router.post('/new')
async def create_purpose(purposes: Puproses):
    purposes.set(purposes.user_id, purposes.purposes)


@purposes_router.get('/{subject}/edit')
async def get_edit_purpose():
    return


@purposes_router.put('/{subject}/edit')
async def update_purpose(subject: str, user_id: int, new_purpose: float):
    _purposes: dict = purposes.get(user_id)
    _purposes[subject] = new_purpose
    purposes.set(user_id, _purposes)


@purposes_router.delete('/{subject}')
async def remove_purpose(subject: str, user_id: int):
    _purposes: dict = purposes.get(user_id)
    _purposes[subject] = None
    purposes.set(user_id, _purposes)
