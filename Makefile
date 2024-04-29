install:
	docker-compose build

up:
	docker-compose up --force-recreate

update:
	poetry update

lint:
	poetry run flake8

test:
	poetry run pytest dnevnik365/backend/tests/*.py

test-cov:
	poetry run pytest --cov dnevnik365.backend.tests
