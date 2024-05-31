from fastapi import APIRouter

from datetime import date
from typing import List, Dict

from dnevnik365.scripts.base import BaseStudentDnevnik
from dnevnik365.core.database import homeworks as r
from dnevnik365.models.pydantic import Homework


homework_router = APIRouter(prefix='/homework')


@homework_router.on_event('shutdown')
async def on_shutdown():
    await r.close()


@homework_router.post('/')
async def get_homework(dnevnik_obj: BaseStudentDnevnik, period: List[date] = None) -> Dict[date, Dict[str, str]]:
    return await dnevnik_obj.get_homework(period=period)


@homework_router.put('/')
async def update_status(homework: Homework):
    homeworks: dict | None = r.get(homework.user_id)
    if homeworks is None:
        homeworks = {}
    homeworks[homework.date][homework.lesson] = homework.is_done
    r.set(homework.user_id, homeworks)
