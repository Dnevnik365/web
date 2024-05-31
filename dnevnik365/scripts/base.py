from pydantic import BaseModel
from typing import List, Dict
from datetime import date


class BaseDnevnik(BaseModel):
    pass


class BaseStudentDnevnik(BaseDnevnik):
    def __init__(self, login: str = None, password: str = None):
        return

    async def get_homework(self, period: List[date]) -> Dict[date, Dict[str, str]]:
        return

    async def get_today_marks(self):
        return

    async def get_average_marks(self):
        return

    async def get_school_timetable(self, period: List[date]) -> Dict[date, List[str]]:
        return
