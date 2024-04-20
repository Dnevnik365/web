FROM python:3.12.2

WORKDIR /app

COPY . /app/

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install


CMD ["uvicorn", "dnevnik365.backend.api.app:app", "--host", "0.0.0.0", "--port", "8000"]

EXPOSE 8000
