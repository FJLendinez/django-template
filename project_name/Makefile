NODE_ENV=production

run_dev:
	@poetry run gunicorn --reload config.wsgi
.PHONY: run_dev

run_prod:
	@poetry run gunicorn config.wsgi
.PHONY: run_prod

cssdev:
	@npx tailwindcss -o ./apps/static/tailwind.css --minify -w
.PHONY: cssdev
