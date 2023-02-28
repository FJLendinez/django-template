# {{ project_name }}


## Prerequisites

- `Python 3.10+`
- `Poetry 1.2+`
- `Postgresql 10+`

## Development

### Create a new virtual environment

```shell
poetry shell
```
### Install dependencies

```shell
poetry install
```

### Install pre-commit

```shell
pre-commit install
```

### Run the django development server

```
make run_dev
```

### Compile tailwind in watch mode

Open a new terminal and run

```shell
make cssdev
```
