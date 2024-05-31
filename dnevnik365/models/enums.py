from enum import Enum


class Role(str, Enum):
    teacher = 'teacher'
    student = 'student'


class Purpose(float, Enum):
    _2_5 = 2.5
    _3 = 3.0
    _3_5 = 3.5
    _4 = 4.0
    _4_5 = 4.5
    _5 = 5.0


class Service(str, Enum):
    dnevnikru = 'dnevnikru'
    ballovnet = 'ballovnet'
    eljur = 'eljur'
    kirov_education = 'kirov_education'
