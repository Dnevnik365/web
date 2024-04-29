from sqlalchemy.ext.asyncio import create_async_engine
from dnevnik365.backend.api.settings import DATABASE_URL


engine = create_async_engine(DATABASE_URL)
