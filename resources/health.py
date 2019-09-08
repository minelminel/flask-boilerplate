from flask import request
from flask_restful import Resource, Api


class HealthResource(Resource):
    def get(self):
        return {'running':True}

    def post(self):
        return {'running':False}
