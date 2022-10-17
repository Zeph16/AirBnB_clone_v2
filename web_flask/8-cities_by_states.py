#!/usr/bin/python3
""" Script that runs a flask web app """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """ 'tears down' the sql alchemy session """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def display_html():
    """ provides content for the /cities_by_states route """
    states = storage.all(State)
    return render_template('8-cities_by_states.html',
                           Table="States",
                           states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
