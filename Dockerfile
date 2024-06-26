FROM python:3.12.2

WORKDIR /dnevnik365

COPY . /dnevnik365/

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install


CMD ["poetry", "run", "uvicorn", "dnevnik365.api.app:app", "--host", "0.0.0.0", "--port", "8000", "--log-config=log_config.ini", "--log-level=debug", "--reload", "--reload-dir", "."]

EXPOSE 8000
