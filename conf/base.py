import os

SERVICE_ID = 'test-service'

BASEDIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
LOGDIR = os.path.join(BASEDIR, 'logs')
DOMAIN = os.getenv("DOMAIN", default="example.com")
ALLOW_METHODS = ("GET", "POST", "PUT", "DELETE", "OPTIONS")

FILTERS = [
    'flask_mico.filters.Translate'
]
EXTENSIONS = [
]