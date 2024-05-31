from pydantic import BaseModel

from typing import Optional, Dict
from datetime import date

from dnevnik365.models.enums import Role, Purpose, Service


class User(BaseModel):
    id: int = None
    name: Optional[str] = None
    login: str
    password: str
    role: Role
    service: Service


class Puproses(BaseModel):
    user_id: int
    purposes: Dict[str, Purpose] = {}


class Homework(BaseModel):
    user_id: int
    date: date
    lesson: int
    is_done: bool = False
