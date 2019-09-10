from flask import request
from flask_restful import Resource, Api


class HealthResource(Resource):
    def get(self):
        return 'running'

    def post(self):
        return 'running'
