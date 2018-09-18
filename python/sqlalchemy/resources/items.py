from flask_restplus import Resource
from flask_restplus import  reqparse
from flask_jwt import jwt_required
from http import  HTTPStatus
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("price", type=float, required=True)

    @jwt_required()
    def get(self, name):
        item = ItemModel.get_item(name)
        print(item)
        return item.json(), HTTPStatus.OK if item else HTTPStatus.BAD_REQUEST


    def post(self, name):

        if ItemModel.get_item(name):
            return {"message": "{} item already exists".format(name)}

        print("name {}".format(name))

        data = Item.parser.parse_args()

        item = ItemModel(name, data["price"])
        item.insert()

        return item.json(), HTTPStatus.CREATED

class Items(Resource):
    def get(self):
        return ItemModel.fetchall()