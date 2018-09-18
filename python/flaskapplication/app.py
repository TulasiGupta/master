from http import HTTPStatus

from flask import  Flask
from flask_restplus import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = "tcheedel"
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth

items = []

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("price", type=float, required=True)

    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {"item":item}, HTTPStatus.OK if item else HTTPStatus.BAD_REQUEST


    def post(self, name):
        data = Item.parser.parse_args()
        item = next(filter(lambda x: x['name'] == name, items), None)

        if item:
            return {"message": "{} item already exists".format(item)}

        item = {"name":name, "price":data["price"]}
        items.append(item)
        return item, HTTPStatus.CREATED

class Items(Resource):
    def get(self):
        return items

api.add_resource(Items, '/items')
api.add_resource(Item, '/items/<string:name>')

app.run(port=5000, debug=True)

