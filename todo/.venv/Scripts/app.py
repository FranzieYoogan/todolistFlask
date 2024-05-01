from ast import parse
from flask import Flask, render_template
app = Flask(__name__)
from db import *


@app.route("/")
def home():
    data = result[0][2]
    
 

    return render_template('home.htm',data = str(data))


app.run(debug=True) 