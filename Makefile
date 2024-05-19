build:
	sudo docker-compose build

start:
	sudo docker-compose up --force-recreate --remove-orphans

up:
	sudo docker-compose up --force-recreate --remove-orphans -d

stop:
	sudo docker-compose stop

rm:
	sudo docker-compose rm
	sudo rm -rf db

db-upgrade:
	poetry run alembic upgrade $(revision)

db-downgrade:
	poetry run alembic downgrade $(revision)

update:
	poetry update

lint:
	poetry run flake8
	poetry run pyright

test:
	poetry run pytest dnevnik365/backend/tests/*.py

test-cov:
	poetry run pytest --cov dnevnik365.backend.tests
