#!/usr/bin/python3
""" Script that runs a flask web app"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ returns content for /route """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ returns content for /hbnb """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ returns content for /c/<text> """
    return 'C %s' % text.replace('_', ' ')

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="cool"):
    """ returns content for /python/<text> """
    return 'Python %s' % text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """ returns content for /number/<n> route """
    return "%d is a number" % n

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ returns content for /number_template/<n> route """
    return render_template('5-number.html', num=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """ returns content for /number_odd_or_even/<n> route """
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html', num=n, parity="even")
    return render_template('6-number_odd_or_even.html', num=n, parity="odd")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
