.PHONY: setup-dev setup-prd build-dev build-prd up-dev ps down python

setup:
	@make build
	@make up
	@make ps

build:
	docker compose build --no-cache

up:
	docker compose up -d

ps:
	docker compose ps

down:
	docker compose down
