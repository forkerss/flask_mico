from flask import g, request

from app.lib import errors
from app.log import logger


def on_json_loading_failed(e):
    raise errors.InvalidParameterError(
        "Failed to decode JSON object: {0}".format(e))


class Translate:
    """Translate
        - application/json
    """

    def process_request(self):
        logger.debug("Translate - method: %s, content_type: %s",
                     repr(request.method), repr(request.content_type))
        if not request.is_json:
            return
        request.on_json_loading_failed = on_json_loading_failed
        raw_json = request.get_json()
        if not isinstance(raw_json, dict):
            raise errors.InvalidParameterError(
                "A valid JSON document is required")
        g.data = raw_json
