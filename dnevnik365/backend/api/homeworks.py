from fastapi import APIRouter

from datetime import date
from typing import List, Dict

from dnevnik365.backend.scripts.base import BaseStudentDnevnik
from dnevnik365.backend.api.database import homeworks
from dnevnik365.backend.models.pydantic_models import Homework


homework_router = APIRouter(prefix='homework')


@homework_router.post('/')
async def get_homework(dnevnik_obj: BaseStudentDnevnik, period: List[date] = None) -> Dict[date, Dict[str, str]]:
    return await dnevnik_obj.get_homework(period=period)


@homework_router.put('/')
async def update_status(homework: Homework):
    _homeworks: dict | None = homeworks.get(homework.user_id)
    if _homeworks is None:
        _homeworks = {}
    _homeworks[homework.date][homework.lesson] = homework.is_done
    homeworks.set(homework.user_id, _homeworks)
