import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "create table users(id int, username text, password text)"

cursor.execute(create_table)

users = [(1, "User1", "Pass1"),
(2, "User2", "Pass2"),
(3, "User3", "Pass3")]

insertquery = "insert into users values (?, ?, ?)"

#cursor.execute(insertquery, users[0])

cursor.executemany(insertquery, users)

connection.commit()


selectquery = "select * from users"

for row in cursor.execute(selectquery):
    print(row)

connection.close()