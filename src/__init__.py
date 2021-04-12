from flask import Flask
from flask_restful import Api

from src.routes import Home, Smoke

app = Flask(__name__)
api = Api(app)


api.add_resource(Home, '/', strict_slashes=False)
api.add_resource(Smoke, '/smoke', strict_slashes=False)





