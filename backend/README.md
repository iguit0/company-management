# Company API

A lightweight RESTful service for managing company's data.

## Technologies

- [Python 3.11](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/2.3.x/)
- [Mypy](https://mypy-lang.org/)
- [Docker](https://www.docker.com/)
  - [Docker-Compose](https://docs.docker.com/compose/)

## Features

- [x] CRUD
- [x] Linting
- [x] Docker Integration
- [ ] Documentation
- [ ] Unit Testing with Pytest

## Configuration

1. Create a virtual environment

```shell
    make build-venv
```

2. Activate the virtual environment

```shell
    source venv/bin/activate
```

3. Install dependencies

```shell
    make requirements-dev 
```

## Linting

Run lint and type checkers to reformat files before commit

```shell
    make lint
```

## Running

(Recommended) Using docker:
```shell
    docker-compose up
```

Or if you prefer to supress logs:
```shell
    docker-compose up -d
```

Or you can run in standalone:

```shell
    make run-dev
```

PS: You should be in the virtual env that you created in first steps.

You can use Postman, Insomnia or whatever REST Client you want.

I use a [REST Client extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) built in VSCode. Easy to use. Check [collection.rest](/backend/collection.rest).

## Database

The "database" is located in [backend/app/data/companies.json](/backend/app/data/companies.json)

