"""app
"""
import os

from flask import Flask

from app.api.v1.test import TestApi
from app.extensions import db
from app.filters import Translate
from app.lib.errors import register_errors
from app.lib.register_filter import register_filters
from app.log import LOGLEVELS, setup_logger
from app.settings import config


def register_extensions(app):
    db.init_app(app)


def register_api(app, version="/v1"):
    def add_url_rule(path, api_cls):
        app.add_url_rule(
            version+path, view_func=api_cls.as_view(api_cls.__name__))

    add_url_rule('/index', TestApi)


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    # setup logger
    setup_logger(level=LOGLEVELS[config_name])

    register_extensions(app)
    register_errors(app)
    register_api(app)
    register_filters(app, filters=[Translate()])

    return app
