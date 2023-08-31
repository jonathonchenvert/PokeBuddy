CURRENT_DIRECTORY := $(shell pwd)

TESTSCOPE = pokebuddy
TESTFLAGS = --with-timer --timer-top-n 10 --keepdb

help:
	@echo "Docker Compose Help"
	@echo "-----------------------"
	@echo ""
	@echo "Run tests to ensure current state is good:"
	@echo "    make test"
	@echo ""
	@echo "If tests pass, add fixture data and start up the api:"
	@echo "    make begin"
	@echo ""
	@echo "Really, really start over:"
	@echo "    make clean"
	@echo ""
	@echo "See contents of Makefile for more targets."

begin: migrate fixtures start

start:
	@docker-compose up -d

stop:
	@docker-compose stop

status:
	@docker-compose ps

restart: stop start

clean: stop
	@docker-compose rm --force
	@find . -name \*.pyc -delete

build:
	@docker-compose build

test:
	@docker-compose run --rm web python ./manage.py test 

coverage:
	@docker-compose run --rm web coverage run ./manage.py test -v 2
	@docker-compose run --rm web coverage html

testwarn:
	@docker-compose run --rm web python -Wall manage.py test ${TESTSCOPE} ${TESTFLAGS}

migrations:
	@docker-compose run --rm web python ./manage.py makemigrations

migrate:
	@docker-compose run --rm web python ./manage.py migrate

superuser:
	@docker-compose run --rm web python ./manage.py createsuperuser

fixtures:
	@docker-compose run --rm web python ./manage.py runscript load_all_fixtures

cli:
	@docker-compose run --rm web bash

tail:
	@docker-compose logs -f

db-shell:
	@docker-compose run db psql -h db -U postgres

.PHONY: start stop status restart clean build test testwarn migrate fixtures cli tail db-shell%                                                                     ➜  marioparty-django 
