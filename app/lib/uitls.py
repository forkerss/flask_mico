"""
"""
from werkzeug.http import HTTP_STATUS_CODES


def http_status_message(code):
    """Maps an HTTP status code to the textual status"""
    return HTTP_STATUS_CODES.get(code, '')
