from pydantic import BaseModel

from typing import Optional, Dict
from datetime import date
from enum import Enum


class Service(Enum):
    dnevnikru = 'dnevnikru'
    ballovnet = 'ballovnet'
    eljur = 'eljur'
    kirov_education = 'kirov_education'


class PurposeValue(Enum):
    _2_5 = 2.5
    _3 = 3.0
    _3_5 = 3.5
    _4 = 4.0
    _4_5 = 4.5
    _5 = 5.0


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
    purposes: Dict[str, PurposeValue] = {}


class Homework(BaseModel):
    user_id: int
    date: date
    lesson: int
    is_done: bool = False
