from pydnevnikruapi.aiodnevnik import AsyncDiaryAPI
from datetime import date
from dnevnik365.backend.scripts.base import BaseStudentDnevnik


class StudentDnevnik(AsyncDiaryAPI, BaseStudentDnevnik):
    def __init__(self, login: str = None, password: str = None):
        super().__init__(login, password)

    async def get_homework(self):
        return await super().get_person_homework(person_id=await self.get_info(), school_id=await self.get_school())

    async def get_today_marks(self):
        return await super().get_marks_by_date(person_id=await self.get_info())

    async def get_average_marks(self):
        return await super().get_person_average_marks(await self.get_info(), int(date.today()))

    async def get_school_timetable(self):
        return await super().get_school_timetable(await self.get_school())
