build:
	docker build -t `basename "${PWD}"` --build-arg uid=`id -u` --build-arg gid=`id -g` --build-arg user=`whoami` -f docker/Dockerfile .
.PHONY: build

run:
	@docker compose -f docker/docker-compose.yml up
.PHONY: run

rundeps:
	@docker compose -f docker/docker-compose.dev.yml -f docker/docker-compose.yml up -d redis postgres
.PHONY: rundeps

rundev:
	@docker compose -f docker/docker-compose.dev.yml -f docker/docker-compose.yml up -d redis postgres
	@docker compose -f docker/docker-compose.dev.yml -f docker/docker-compose.yml up app
.PHONY: rundev

exec:
	@docker exec -it {{project_name}}_app python manage.py shell
.PHONY: exec

bash:
	@docker exec -it {{project_name}}_app bash
.PHONY: bash

cssdev:
	@docker exec -u root -it {{project_name}}_app tailwindcss -o ./static/tailwind.css --minify -w
.PHONY: cssdev
