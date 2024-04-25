from dotenv import load_dotenv
from os import environ


load_dotenv()

DB_USERNAME = environ.get('DB_USERNAME', 'postgres')
DB_PASSWORD = environ.get('DB_PASSWORD', 'postgres')
DB_HOST = environ.get('DB_HOST', 'localhost')
DB_PORT = int(environ.get('DB_PORT'))
DATABASE_URL = f'postgresql+asyncpg://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}'
