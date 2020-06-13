"""middlewares

Example:

    class MiddlewareExample:
        def process_request(self):
            # https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.before_request
            
            # do_somethings
            print("MiddlewareExample", process_request)
        
        def process_response(self,resp):
            # https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.after_request
            
            # do_somethings
            print("MiddlewareExample", process_response)
            return resp

Usage:

    # in settings
    MIDDLEWARES = [
        ...
        'api.middlewares.MiddlewareExample'
        ...
    ]
"""
