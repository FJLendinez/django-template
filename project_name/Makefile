NODE_ENV=production


rundev:
	@poetry run gunicorn --reload --reload-extra-file templates/pages/* --reload-extra-file templates/components/* config.wsgi
.PHONY: run_dev

runprod:
	@poetry run gunicorn config.wsgi
.PHONY: run_prod

cssdev:
	@npx tailwindcss -o ./static/tailwind.css --minify -w
.PHONY: cssdev

build:
	docker build -t `basename "${PWD}"`  -f docker/Dockerfile .
.PHONY: build