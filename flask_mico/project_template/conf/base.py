import os

SERVICE_NAME = '{{project_name}}'
DOMAIN = os.getenv("DOMAIN", default="example.com")

ALLOW_METHODS = ("GET", "POST", "PUT", "DELETE", "OPTIONS")
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
LOG_DIR = os.path.join(BASE_DIR, 'logs')

MIDDLEWARES = [
    'flask_mico.middleware.Translate'
]

EXTENSIONS = [
]

ROOT_URLCONF = '{{project_name}}.urls'
