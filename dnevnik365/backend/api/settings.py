from dotenv import load_dotenv
from os import environ


load_dotenv()

DB_USERNAME = environ.get('POSTGRES_USERNAME', 'postgres')
DB_PASSWORD = environ.get('POSTGRES_PASSWORD', 'postgres')
DB_HOST = environ.get('POSTGRES_HOST', 'localhost')
DB_PORT = int(environ.get('POSTGRES_PORT', 5432))
DATABASE_URL = f'postgresql+asyncpg://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}'
