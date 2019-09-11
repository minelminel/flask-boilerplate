from flask import current_app
from flask import request, jsonify
from flask_restful import Resource


class IndexResource(Resource):
    def get(self):
        return str(current_app.config)
