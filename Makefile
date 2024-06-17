build:
	poetry run docker-compose build

start:
	poetry run docker-compose up --force-recreate --remove-orphans

up:
	poetry run docker-compose up --force-recreate --remove-orphans -d

stop:
	poetry run docker-compose stop

rm:
	poetry run docker-compose rm
	sudo rm -rf db

db-upgrade:
	poetry run alembic upgrade $(revision)

db-downgrade:
	poetry run alembic downgrade $(revision)

update:
	poetry update

lint:
	poetry run flake8
	poetry run mypy -p dnevnik365

test:
	poetry run pytest dnevnik365/backend/tests/*.py

test-cov:
	poetry run pytest --cov dnevnik365.backend.tests
