from dotenv import load_dotenv
from os import environ


load_dotenv()

HOST = environ.get('HOST', 'localhost')

DB_NAME = environ.get('POSTGRES_NAME', 'postgres')
DB_USERNAME = environ.get('POSTGRES_USERNAME', 'postgres')
DB_PASSWORD = environ.get('POSTGRES_PASSWORD', 'postgres')
DB_PORT = int(environ.get('POSTGRES_PORT', 5432))

REDIS_USER = environ['REDIS_USER']
REDIS_PASSWORD = environ['REDIS_PASSWORD']

DATABASE_URL = f'postgresql+asyncpg://{DB_USERNAME}:{DB_PASSWORD}@{HOST}:{DB_PORT}/{DB_NAME}'
