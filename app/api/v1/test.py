from flask import g

from lib import ApiView, validator
from lib.error import InvalidParameterError


class TestApi(ApiView):
    @validator(schema=FIELDSCHEMAS['Test'])
    def get(self):
        print(g.data)
        # raise InvalidParameterError("test")
        return self.on_success(msg="hello", data=g.data)

    def post(self):
        return self.on_success(msg="hello", data={"HAHA": 121})
