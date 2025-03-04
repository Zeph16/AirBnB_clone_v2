#!/usr/bin/python3
""" Script that runs a flask web app"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ returns content for /route """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ returns content for /route """
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
