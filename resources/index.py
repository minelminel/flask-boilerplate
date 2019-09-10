from flask import request, jsonify
from flask_restful import Resource


class IndexResource(Resource):
    def get(self):
        return jsonify(dict(app.config))