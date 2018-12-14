import os
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://hiteshpr:hitesh12345@ds037758.mlab.com:37758/legal_ai"
mongo = PyMongo(app)


@app.route('/')
def hello():
    return "Hello World, Legal AI!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()