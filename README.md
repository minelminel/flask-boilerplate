[![Build Status](https://travis-ci.org/minelminel/flask-boilerplate.svg?branch=master)](https://travis-ci.org/minelminel/flask-boilerplate)

# Flask Boilerplate :potable_water:

This repository contains a sample minimal Flask application structure that includes:

* SQLAlchemy
* Alembic
* Celery
* Pytest
* Coverage

It runs on Python 3.x

## Installation

First, clone the repository and create a virtualenv. Then install the requirements:

`$ pip install -e .`

Before running the application make sure that your local PostgreSQL server is up. Then create the databases:

```sql
CREATE DATABASE flask_example;
CREATE DATABASE flask_example_test;
```

Now you can create the tables using Alembic:
```bash
webapp db upgrade
```

Finally you can run the application:
```bash
webapp runserver
```

or play in the Python REPL:
```bash
webapp shell
```

In order to run unit tests in py.test invoke:
```bash
webapp test
```

To view test coverage:
```bash
webapp coverage
```

There is a preconfigured WSGI module located at `webapp.core.wsgi`. Example usage with Gunicorn:
```bash
gunicorn --workers 1 --bind 0.0.0.0:8000 webapp.core.wsgi:application
```

If the process fails to start, try prepending the `gunicorn` with its relative path within your virtual environment, for example `env/bin/gunicorn ...`
