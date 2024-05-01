import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="",
  database="todo_schema"
)

mycursor = mydb.cursor()

mycursor.execute("select * from todoTask")
result = mycursor.fetchall()
print(result)