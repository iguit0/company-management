# Company API

A lightweight RESTful service for managing company's data.

### Technologies

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

### Configuration

1. Create a virtual environment

```shell
    make build-venv
```

2. Activate the virtual environment

```shell
    source venv/bin/activate
```

3. Configure env file

```shell
    make load-env
```

4. Install dependencies

```shell
    make requirements-dev 
```

### Linting

Run lint and type checkers to reformat files before commit

```shell
    make lint
```

### Running

```shell
    make run-dev
```

To open documentation navigate to http://localhost:8000/docs

