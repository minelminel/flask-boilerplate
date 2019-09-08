[![Build Status](https://travis-ci.org/minelminel/flask-boilerplate.svg?branch=master)](https://travis-ci.org/minelminel/flask-boilerplate)

# Flask Boilerplate

This repository contains a sample minimal Flask application structure that includes:

* SQLAlchemy
* Alembic
* Celery
* py.test

It runs on both Python 2.7 and 3.5.

## Installation

First, clone the repository and create a virtualenv. Then install the requirements:

`$ pip install -r requirements.txt`

Before running the application make sure that your local PostgreSQL server is up. Then create the databases:

```
CREATE DATABASE flask_example;
CREATE DATABASE flask_example_test;
```

Now you can create the tables using Alembic:

`./manage.py db upgrade`

Finally you can run the application:

`./manage.py runserver`

or play in the Python REPL:

`./manage.py shell`

In order to run unit tests in py.test invoke:

`./manage.py test`


## Contribution

We are happy to see your way of scaffolding Flask applications. Feel free to submit an issue with your ideas or comments.

```
.
├── LICENSE
├── README.md
├── api.py
├── app.py
├── celerybeat-schedule
├── config
│   ├── __init__.py
│   ├── local.py
│   ├── staging.py
│   └── testing.py
├── database.py
├── env
├── manage.py
├── migrations
│   ├── README
│   ├── alembic.ini
│   ├── env.py
│   ├── script.py.mako
│   └── versions
│       └── 40aa1a9694cf_.py
├── requirements.txt
├── tasks.py
├── tests
│   ├── __init__.py
│   ├── client.py
│   ├── command.py
│   ├── conftest.py
│   ├── factories.py
│   └── test_api.py
└── wsgi.py
```

### CI/CD
1. Local development and testing is performed
2. Branch is merged into `staging`
3. New merges trigger automatic builds
4. If build is successful, auto merge to `master`
  - upon failing the build/test, a postmortem report is available for analysis and corrective action
5. Changes to `master` are automatically deployed to production
