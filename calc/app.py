from flask import Flask, request
from operations import*

app = Flask(__name__)

@app.route("/add")
def add_numbers():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return f"{add(a,b)}"

@app.route("/sub")
def subtract_numbers():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return f"{sub(a,b)}"

@app.route("/mult")
def multiply_numbers():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return f"{mult(a,b)}"

@app.route("/div")
def divide_numbers():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return f"{div(a,b)}"

