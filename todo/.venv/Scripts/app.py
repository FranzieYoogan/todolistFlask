from ast import parse
from flask import request
from flask import Flask, render_template
app = Flask(__name__)
from db import *
from datetime import date

@app.route("/",methods=['POST','GET'])
def home():
 data = str(result)
 
 print(data)
    
 if(request.method == "POST"):
  inputValue = request.form['inputValue']
  today = date.today()
  
  if(inputValue):
   cursor.execute(f"insert into todoTask (todoTask,todoDate) values('{inputValue}','{today}')")
   mydb.commit()
   return render_template('home.htm',data = data)
 return render_template('home.htm',data = str(data))


app.run(debug=True) 