from dotenv import load_dotenv
from os import environ


load_dotenv()

HOST = environ.get('POSTGRES_HOST', 'localhost')

DB_NAME = environ.get('POSTGRES_NAME', 'postgres')
DB_USERNAME = environ.get('POSTGRES_USERNAME', 'postgres')
DB_PASSWORD = environ.get('POSTGRES_PASSWORD', 'postgres')
DB_PORT = int(environ.get('POSTGRES_PORT', 5432))

REDIS_PORT = environ.get('REDIS_PORT', 6379)
REDIS_USER = environ.get('REDIS_USER', 'redis')
REDIS_PASSWORD = environ.get('REDIS_PASSWORD', 'redis')

DATABASE_URL = f'postgresql+asyncpg://{DB_USERNAME}:{DB_PASSWORD}@{HOST}:{DB_PORT}/{DB_NAME}'
