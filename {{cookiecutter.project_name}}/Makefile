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
	@mkdir -p ./config/tailwind
	@if [ ! -f ./config/tailwind/tailwindcss ]; then \
  		echo 'Downloading latest version of tailwind' ; \
  		curl -sLo ./config/tailwind/tailwindcss https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-linux-x64 ; \
	fi
	@chmod +x ./config/tailwind/tailwindcss
	@if [ ! -f ./config/tailwind/daisyui.js ]; then \
  		echo 'Downloading latest version of daisyui' ; \
  		curl -sLo ./config/tailwind/daisyui.js https://github.com/saadeghi/daisyui/releases/latest/download/daisyui.js ; \
  		curl -sLo ./config/tailwind/daisyui-theme.js https://github.com/saadeghi/daisyui/releases/latest/download/daisyui-theme.js ; \
	fi
	./config/tailwind/tailwindcss -i tailwind.css -o ./static/tailwind.css --minify -w
.PHONY: cssdev

test:
	@uvx ruff check
	@uv run manage.py test
.PHONY: test

htmxupgrade:
	@curl -o static/htmx.min.js https://unpkg.com/htmx.org@2.0.4/dist/htmx.min.js
.PHONY: htmxupgrade
