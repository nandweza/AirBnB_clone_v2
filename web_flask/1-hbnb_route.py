#!/usr/bin/python3
"""a script that starts a Flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """displays a string at the / route."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """displays a string at the /hbnb route."""
    return 'HBNB'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
