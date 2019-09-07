from flask_restful import Api
from .status import Api_Status
from .health import Api_Health

api = Api()
api.add_resource(Api_Status, '/status')
api.add_resource(Api_Health, '/health')
