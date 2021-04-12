from flask_restful import Resource
from src import api


class Home(Resource):
    def get(self):
        return {"message": "This is home page"}, 200


class Smoke(Resource):
    def get(self):
        return {"message": "Ok"}, 200


api.add_resource(Home, '/')
api.add_resource(Smoke, '/smoke')


