include .env

db_drop:
	@@PGPASSWORD=$(DB_PASSWD) dropdb --if-exists -U $(DB_USER) -h $(DB_HOST) $(DB_NAME);

db_create:
	@@PGPASSWORD=$(DB_PASSWD) createdb -U $(DB_USER) -h $(DB_HOST) $(DB_NAME);

db_migrate:
	@@steradian makemigrations
	@@steradian migrate
	@@steradian migrate --run-syncdb

db_reset: db_drop db_create db_migrate

build:
	@@rm -rf dist
	@@poetry build
