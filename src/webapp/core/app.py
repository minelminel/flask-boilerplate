import os

from celery import Celery
from flask import Flask

from webapp.models import migrate, db
from webapp.resources import api


config_variable_name = 'FLASK_CONFIG_PATH'
default_config_path = os.path.join(os.path.dirname(__file__), '../config/local.py')
os.environ.setdefault(config_variable_name, default_config_path)


def create_app(config_file=None, settings_override=None):
    app = Flask(__name__)

    if config_file:
        app.config.from_pyfile(config_file)
    else:
        app.config.from_envvar(config_variable_name)

    if settings_override:
        app.config.update(settings_override)

    init_app(app)
    setup_logging(app)

    return app


def init_app(app):
    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)
    # this is where the magic happens
    # avoid contextual errors by including all modules atomically HERE


def setup_logging(app):
    if not app.debug:
        import logging
        from logging import FileHandler
        handler = FileHandler('flask.log')
        handler.setLevel(logging.DEBUG)
        app.logger.addHandler(handler)


def create_celery_app(app=None):
    app = app or create_app()
    celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery
