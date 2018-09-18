from db import db
from sqlalchemy import Column, Integer, String, Float

class UserModel(db.Model):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(80))
    password = Column(String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def createuser(self):
        db.session.add(self)
        db.session.commit()