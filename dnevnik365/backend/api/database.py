from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import create_async_engine
from dnevnik365.backend.api.settings import DATABASE_URL, REDIS_USER, REDIS_PASSWORD, HOST


engine = create_async_engine(DATABASE_URL)
purposes = Redis(host=HOST, port=6378, username=REDIS_USER, password=REDIS_PASSWORD)
timetable = Redis(host=HOST, port=6380, username=REDIS_USER, password=REDIS_PASSWORD)
