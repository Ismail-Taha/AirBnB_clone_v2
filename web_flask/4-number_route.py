#!/usr/bin/python3
"""
start Flask application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """return Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ return HBNB """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """display “C ” followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Display 'Python ' followed by the value of the text variable,
    with underscores replaced by spaces. Default value is 'is cool'."""
    modified_txt = text.replace('_', ' ')
    return 'Python ' + modified_txt


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """Display 'n is a number' only if n is an integer."""
    return f'{n} is a number'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
