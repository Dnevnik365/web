from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from pydantic import BaseModel

from typing import Optional, Dict, List
from datetime import date


metadata = MetaData()


class Base(DeclarativeBase):
    pass


class User(BaseModel):
    id: int = None
    name: Optional[str] = None
    login: str
    password: str
    role: str
    service: str


class UserModel(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(nullable=True)
    login: Mapped[str]
    password: Mapped[str]
    role: Mapped[str]
    service: Mapped[str]


class Puproses(BaseModel):
    user_id: int
    purposes: Dict[str, float] = {}


class Timetable(BaseModel):
    user_id: int
    timetable: Dict[date, List[str]] = {}
