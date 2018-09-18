from flask import  Flask
from flask_restplus import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.items import Items, Item
from models.user import UserModel

app = Flask(__name__)
app.secret_key = "tcheedel"
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
app.config['PROPAGATE_EXCEPTIONS'] = True
#app.config['JWT_AUTH_URL_RULE'] = '/login'

@app.before_first_request
def create_tables():
    db.create_all()
    usermodel = UserModel("User1", "Pass1")
    usermodel.createuser()

jwt = JWT(app, authenticate, identity) # /auth

items = []



api.add_resource(Items, '/items')
api.add_resource(Item, '/items/<string:name>')

if __name__ == '__main__':
    from db import db
    db.init_app(app=app)
    app.run(port=5000, debug=True)

