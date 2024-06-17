<p align="center">
    <a href="https://github.com/Dnevnik365/web/blob/dev/LICENSE">
        <img alt="license" src="https://img.shields.io/github/license/Dnevnik365/web?label=License&color=green&style=for-the-badge">
    </a>
    <img alt="python" src="https://img.shields.io/badge/3.12.2-green?color=green&label=Python&style=for-the-badge">
</p>

<h1 align="center">Дневник 365</h1>


## ✍ Описание

Веб-сервис для взаимодействия с несколькими электронными дневниками


## 🛠 Команды для запуска

Нужно чтобы `git`, `make`, `docker` и `docker-compose` были установлены

Скачать проект с гитхаба
```bash
git clone https://github.com/Dnevnik365/web/
```
<br>

Установить зависимости
```bash
make build
```
<br>

Обновить зависимости
```bash
make update
```
<br>

Запустить проект
```bash
make start
```
<br>

Запустить проект в фоновом режиме
```bash
make up
```
<br>

Остановить контейнеры
```bash
make stop
```
<br

Удалить контейнеры и данные из БД
```bash
make rm
```
<br>

Запустить обновление БД(для последней версии укажите `revision=head`)
```bash
make db-upgrade revision=<версия>
```
<br>

Запустить откат БД
```bash
make db-downgrade revision=<версия>
```
<br>

Проверить читаемость кода
```bash
make lint
```
<br>

Запустить все тесты
```bash
make test
```
<br>

Проверить покрытие кода тестами
```bash
make test-cov
```


## 🖥 Переменные окружения

Ниже все нужные переменные окружения. Примеры [здесь](https://github.com/Dnevnik365/web/blob/dev/.env.example)

- `HOST` - хост сервера

- `POSTGRES_USER` - юзернейм для базы данных postgres

- `POSTGRES_PASSWORD` - пароль для БД

- `POSTGRES_PORT` - порт БД

- `POSTGRES_DB` - название БД

- `REDIS_PASSWORD` - пароль для баз данных redis

- `HOMEWORK_DB_PORT` - порт для бд с домашними заданиями

- `PURPOSES_DB_PORT` - порт для бд с целями


## 💿 [Зависимости](https://github.com/Dnevnik365/web/blob/dev/pyproject.toml)

- **[fastapi](https://pypi.prg/project/fastapi) - 0.110.2**

- **[asyncpg](https://pypi.prg/project/asyncpg) - 0.29.0**

- **[python-dotenv](https://pypi.prg/project/python-dotenv) - 1.0.1**

- **[jinja2](https://pypi.prg/project/jinja2) - 3.1.4**

- **[python-multipart](https://pypi.prg/project/pyhton-multipart) - 0.0.9**

- **[uvicorn](https://pypi.prg/project/uvicorn) - 0.29.0**

- **[pydnevnikruapi](https://pypi.prg/project/pydnevnikruapi) - 0.1.1**

- **[sqlalchemy](https://pypi.prg/project/sqlalchemy) - 2.0.29**

- **[redis](https://pypi.prg/project/redis) - 5.0.4**

- **[alembic](https://pypi.prg/project/alembic) - 1.13.1**

- **[aiohttp](https://pypi.prg/project/aiohttp) - 3.9.5**

- **[flake8](https://pypi.prg/project/flake8) - 7.0.0**

- **[pytest](https://pypi.prg/project/pytest) - 8.1.1**

- **[pytest-cov](https://pypi.prg/project/pytest-cov) - 5.0.0**

- **[mypy](https://pypi.prg/project/mypy) - 1.10.0**

- **[httpx](https://pypi.prg/project/httpx) - 0.27.0**
