from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import create_async_engine
from dnevnik365.backend.api.settings import DATABASE_URL, REDIS_USER, REDIS_PASSWORD, HOST


engine = create_async_engine(DATABASE_URL)
purposes = Redis(HOST, 6379, username=REDIS_USER, password=REDIS_PASSWORD)
timetable = Redis(HOST, 6380, username=REDIS_USER, password=REDIS_PASSWORD)
