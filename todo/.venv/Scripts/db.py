import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="",
  database="todo_schema"
)

cursor = mydb.cursor()

cursor.execute("select * from todoTask")
result = cursor.fetchall()

