from fastapi import APIRouter

from datetime import date
from typing import List, Dict

from dnevnik365.backend.scripts.base import BaseStudentDnevnik


homework_router = APIRouter(prefix='/homework')


@homework_router.post('/')
async def get_homework(dnevnik_obj: BaseStudentDnevnik, period: List[date] = None) -> Dict[date, Dict[str, str]]:
    return await dnevnik_obj.get_homework(period=period)
