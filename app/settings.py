import os

BASEDIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
LOGDIR = os.path.join(BASEDIR, 'logs')
SERVICE_ID = 'test-service'


class BaseConfig:
    DOMAIN = os.getenv("DOMAIN", default="example.com")
    ALLOW_METHODS = ("GET", "POST", "PUT", "DELETE", "OPTIONS")
    # database
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL', 'sqlite:///' + os.path.join(BASEDIR, 'data.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
