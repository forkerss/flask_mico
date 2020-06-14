"""errors
Example:

1. 
    from enum import Enum
    class APIError(Enum):
        SESSION_EXPIRED = {
            "status": 400,
            "code": 1001,
            "message": "session has expired"
        }
2. 
    SESSION_EXPIRED = {
            "status": 400,
            "code": 1001,
            "message": "session has expired"
    }

Usage:

    ...
    from flask_mico.error import AppError
    class Index(ApiView):
        def get(self):
            # raise AppError(SESSION_EXPIRED) or /
            raise AppError(APIError.SESSION_EXPIRED)
    ...
"""
