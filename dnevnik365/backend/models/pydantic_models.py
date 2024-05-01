from pydantic import BaseModel

from typing import Optional, Dict, List
from datetime import date
from enum import Enum


class Service(Enum):
    dnevnikru = 'dnevnikru'
    ballovnet = 'ballovnet'
    eljur = 'eljur'
    kirov_education = 'kirov_education'


class Role(Enum):
    teacher = 'teacher'
    student = 'student'


class User(BaseModel):
    id: int = None
    name: Optional[str] = None
    login: str
    password: str
    role: Role
    service: Service


class Puproses(BaseModel):
    user_id: int
    purposes: Dict[str, float] = {}


class Timetable(BaseModel):
    user_id: int
    timetable: Dict[date, List[str]] = {}
