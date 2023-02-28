NODE_ENV=production

run_dev:
	@poetry run gunicorn --reload --reload-extra-file templates/* main.wsgi
.PHONY: run_dev

run_schedule:
	@poetry run python manage.py runschedule
.PHONY: run_dev

run_prod:
	@poetry run gunicorn main.wsgi
.PHONY: run_prod

cssdev:
	@npx tailwindcss -o ./static/tailwind.css --minify -w
.PHONY: cssdev
