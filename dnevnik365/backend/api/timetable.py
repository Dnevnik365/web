from fastapi import APIRouter

from datetime import date
from typing import List, Dict

from dnevnik365.backend.scripts.base import BaseStudentDnevnik


timetable_router = APIRouter(prefix='/timetable')


@timetable_router.post('/')
async def get_timetable(dnevnik_obj: BaseStudentDnevnik, period: List[date] = None) -> Dict[date, List[str]]:
    return await dnevnik_obj.get_school_timetable(period=period)
