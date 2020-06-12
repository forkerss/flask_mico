"""main
"""
import os
import importlib

from flask import Flask

from lib.error.err_handle import register_errors
from lib.filter_handle import register_filters
from lib.log import setup_logger
from app.settings import config


# def register_extensions(app):
# db.init_app(app)


def register_api(app, version="/v1"):
    def add_url_rule(path, api_cls):
        app.add_url_rule(
            version+path, view_func=api_cls.as_view(api_cls.__name__))
    # add_url_rule('/index', TestApi)


def create_app():
    settings = importlib.import_module(
        os.getenv('FLASKMICO_SETTINGS_MODULE', 'conf.development.settings'))
    app = Flask(__name__)
    app.config.from_object(settings)
    # setup logger
    setup_logger()

    # register_extensions(app)
    # register_errors(app)
    # register_api(app)
    # register_filters(app, filters=[Translate()])

    return app
