FROM python:3.11-slim-buster

WORKDIR /code

RUN apt-get update \
    && apt-get install -y build-essential libpq-dev \
    && apt-get install -y libxml2-dev libxslt1-dev libz-dev \
    && apt-get install -y inotify-tools \
    && pip install --upgrade pip \
    && python --version

COPY requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code

EXPOSE 80

ENTRYPOINT ["sh", "/code/docker/entrypoint.sh"]
