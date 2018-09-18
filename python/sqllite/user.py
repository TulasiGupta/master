import sqlite3

class User(object):

    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        print("username "+username)
        connection  = sqlite3.connect("data.db")
        cursor = connection.cursor()
        selectquery = "select * from users where username = ?"
        result = cursor.execute(selectquery, (username,))
        print("result %r", result)
        row = result.fetchone()
        print(row)
        user = None
        if row:
            user = cls(row[0], row[1], row[2])

        connection.close()
        print(user)
        return user

    @classmethod
    def find_by_id(cls, id):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        selectquery = "select * from users where id = ?"
        result = cursor.execute(selectquery, (id,))
        row = result.fetchone()
        user = None
        if row:
            user = cls(row[0], row[1], row[2])

        connection.close()
        print(user)
        return user