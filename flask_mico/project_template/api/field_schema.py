"""field_schema
# https://docs.python-cerberus.org/en/stable/validation-rules.html

Example:
    
    INDEX_POST = {
        "hello": {
            "type": "string",
            "regex": r"^[0-9a-zA-Z_]{4,30}$",
            "required": True
        }
    }

Usage:

    ...
    from flask_mico import validator
    class Index(ApiView):
        @validator(schema=INDEX_POST)
        def get(self):
            return self.on_success(msg="pong", data={"pong": True})
    ...
"""
