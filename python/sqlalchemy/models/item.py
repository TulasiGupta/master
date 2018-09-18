from db import db
from sqlalchemy import Column, Integer, String, Float

class ItemModel(db.Model):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    price = Column(Float(precision=2))

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def get_item(cls, name):
        return ItemModel.query.filter_by(name=name).first()

    def insert(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def fetchall(cls):
            return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}