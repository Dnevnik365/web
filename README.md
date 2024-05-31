<p align="center">
    <a href="https://github.com/Dnevnik365/web/releases">
        <img alt="release" src="https://img.shields.io/github/v/release/Dnevnik365/web?color=green&label=Latest Release&style=for-the-badge&sort=semver">
    </a>
    <a href="https://github.com/Dnevnik365/web/blob/dev/LICENSE">
        <img alt="license" src="https://img.shields.io/github/license/Dnevnik365/web?label=License&color=green&style=for-the-badge">
    </a>
    <img alt="python" src="https://img.shields.io/badge/3.12.2+-green?color=green&label=Python&style=for-the-badge">
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
make up
```
<br>

Остановить все контейнеры и удалить данные из БД
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

- `POSTGRES_PASSWORD` - пароль для базы данных postgres

- `POSTGRES_PORT` - порт для базы данных

- `POSTGRES_NAME` - имя базы данных(по дефолту используется `dnevnik`)

- `REDIS_USER` - юзернейм для базы данных redis

- `REDIS_PASSWORD` - пароль для базы данных redis


## 💿 [Зависимости](https://github.com/Dnevnik365/web/blob/dev/pyproject.toml)

- **[fastapi](https://pypi.org/project/fastapi/) - 0.110.2**

- **[asyncpg](https://pypi.org/project/asyncpg/) - 0.29.0**

- **[python-dotenv](https://pypi.org/project/python-dotenv/) - 1.0.1**

- **[pydantic](https://pypi.org/project/pydantic/) - 2.7.0**

- **[jinja2](https://pypi.org/project/jinja2/) - 3.1.3**

- **[python-multipart](https://pypi.org/project/python-multipart/) - 0.0.9**

- **[fastapi-users](https://pypi.org/project/fastapi-users/) - 13.0.0**

- **[uvicorn](https://pypi.org/project/uvicorn/) - 0.29.0**

- **[httpx](https://pypi.org/project/httpx/) - 0.27.0**

- **[pydnevnikruapi](https://pypi.org/project/pydnevnikruapi/) - 0.1.1**

- **[sqlalchemy](https://pypi.org/project/sqlalchemy/) - 2.0.29**

- **[redis](https://pypi.org/project/aioredis/) - 5.0.4**

- **[flake8](https://pypi.org/project/flake8/) - 7.0.0**

- **[pytest](https://pypi.org/project/pytest/) - 8.1.1**

- **[pytest-cov](https://pypi.org/project/pytest-cov/) - 5.0.0**

- **[alembic](https://pypi.org/project/alembic/) - 1.13.1**

- **[mypy](https://pypi.org/project/pyright) - 1.1.360**
