#!/bin/sh

tailwindcss -i static/css/style.css -o static/css/output.css --minify
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py makesuperuser
gunicorn config.wsgi --config="docker/gunicorn.conf.py"