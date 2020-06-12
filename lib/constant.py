"""
common constant
"""
from werkzeug.http import HTTP_STATUS_CODES

MEDIA_JSON = 'application/json'


def http_status_message(code):
    """Maps an HTTP status code to the textual status"""
    return HTTP_STATUS_CODES.get(code, '')
