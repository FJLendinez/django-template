build:
	docker build -t {{cookiecutter.project_name}} --build-arg uid=`id -u` --build-arg gid=`id -g` --build-arg user=`whoami` -f docker/Dockerfile .
.PHONY: build

run:
	@docker compose -f docker/docker-compose.yml up
.PHONY: run

rundeps:
	@docker compose -f docker/docker-compose.dev.yml -f docker/docker-compose.yml up -d redis postgres
.PHONY: rundeps

rundev:
	@docker compose -f docker/docker-compose.dev.yml -f docker/docker-compose.yml up -d redis postgres
	@docker compose -f docker/docker-compose.dev.yml -f docker/docker-compose.yml up {{cookiecutter.project_name}}_app
.PHONY: rundev

exec:
	@docker exec -it {{cookiecutter.project_name}}_app python manage.py shell
.PHONY: exec

bash:
	@docker exec -it {{cookiecutter.project_name}}_app bash
.PHONY: bash

cssdev:
	@uv run tailwindcss -o ./static/tailwind.css --minify
.PHONY: cssdev

runworker:
	@uv run celery -A config worker -n {{cookiecutter.project_name}} -Q highprio,medprio,celery -B -l info
.PHONY: runworker

test:
	@uvx ruff check
	@uv run manage.py test
.PHONY: test

htmxupgrade:
	@curl -o static/htmx.min.js https://cdn.jsdelivr.net/npm/htmx.org/dist/htmx.min.js
.PHONY: htmxupgrade
