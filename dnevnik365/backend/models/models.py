from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON


metadata = MetaData()

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String, nullable=True),
    Column('password', String, nullable=True),
    Column('role', String, nullable=False),
    Column('service', String, nullable=False)
)

purposes = Table(
    'purposes',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('purposes', nullable=True)
)

timetable = Table(
    'timetable',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('timetable')
)
