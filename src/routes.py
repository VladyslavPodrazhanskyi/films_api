from flask_restful import Resource



class Home(Resource):
    def get(self):
        return {"message": "This is home page"}, 200


class Smoke(Resource):
    def get(self):
        return {"message": "Ok"}, 200




