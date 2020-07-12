from flask import Flask

from flask_mico.conf import settings
from flask_mico.error.err_handle import register_errors
from flask_mico.log import setup_logger
from flask_mico.middleware.mid_handle import register_middlewares
from flask_mico.urls import register_routes
from flask_mico.util import register_commands, register_extensions


def create_app():
    app = Flask(__name__, static_folder=None, template_folder=None)
    app.config.from_object(settings)

    setup_logger(settings.DEBUG, settings.LOG_DIR, settings.SERVICE_NAME)
    register_commands(app, settings.COMMANDS)
    register_middlewares(app, middlewares=settings.MIDDLEWARES)
    register_extensions(app, settings.EXTENSIONS)
    register_routes(app, settings.ROOT_URLCONF)
    register_errors(app)
    return app
