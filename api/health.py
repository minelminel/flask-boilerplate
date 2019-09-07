from flask import request
from flask_restful import Resource, Api

# from database import Document

class Api_Health(Resource):
    def get(self):
        return {'running':True}

    def post(self):
        return {'running':False}
