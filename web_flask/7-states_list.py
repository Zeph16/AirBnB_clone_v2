#!/usr/bin/python3
""" Script that runs a flask web app """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """ 'tears down' the sql alchemy session """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def display_html():
    """ provides content for the /states_list route """
    states = storage.all(State)
    dict_to_html = {value.id: value.name for value in states.values()}
    return render_template('7-states_list.html',
                           Table="States",
                           items=dict_to_html)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
