from ast import parse
import json
import mysql.connector
from flask import request
from flask import Flask, render_template
app = Flask(__name__)
from datetime import date

@app.route("/",methods=['POST','GET'])
def home():
  
 
 
  mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="todo_schema"
    )
  
  cursor = mydb.cursor()

  cursor.execute("select * from todoTask")
  result = cursor.fetchall()
  
  print(result)

  
 
  



  if(request.method == "POST"):


     


      inputValue = request.form['inputValue']
      today = date.today()
      inputValue = request.form['inputValue']
      today = date.today()
      if(inputValue):
        cursor.execute(f"insert into todoTask (todoTask,todoDate) values('{inputValue}','{today}')")
        mydb.commit()
        return render_template('home.htm', data = result)
      else:
        error = True
        return render_template('home.htm',error = error,data = result)
    


  return render_template('home.htm', data = result)

@app.route("/tasks",methods=['POST','GET'])
def tasks():
  
 
  mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="todo_schema"
    )
  
  cursor = mydb.cursor()
  cursor.execute("select * from todoTask")
  result = cursor.fetchall()

  if(request.method == "POST"):
    checkBox = request.form['checkBox']
    cursor.execute(f"DELETE FROM todoTask WHERE todoTask = '{checkBox}'")
    mydb.commit()
    cursor.execute("select * from todoTask")
    result = cursor.fetchall()

    return render_template('tasks.htm',data = result)
  return render_template('tasks.htm',data = result)


app.run(debug=True) 