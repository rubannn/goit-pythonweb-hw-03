.PHONY: all build run stop restart logs clean shell help

IMAGE_NAME = goit-flask-app
CONTAINER_NAME = flask-app
PORT = 3000

build:          ## Збілдити Docker образ
	docker compose build

run:            ## Запустити контейнер
	docker compose up -d

stop:           ## Зупинити контейнер
	docker compose stop

restart:        ## Перезапустити контейнер
	docker compose restart

logs:           ## Переглянути логи
	docker compose logs -f

clean:          ## Зупинити та видалити контейнер, образ і volume
	docker compose down --volumes --rmi local

shell:          ## Зайти всередину контейнера
	docker compose exec app bash

all: build run  ## Збілдити і запустити одразу
