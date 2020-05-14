from flask import g
from app.api.base import Api
from app.lib.errors import InvalidParameterError
from app.lib.field_validator import validator, FIELDSCHEMAS


class TestApi(Api):
    @validator(schema=FIELDSCHEMAS['Test'])
    def get(self):
        print(g.data)
        # raise InvalidParameterError("test")
        return self.on_success(msg="hello", data=g.data)

    def post(self):
        return self.on_success(msg="hello", data={"HAHA": 121})
