#!/usr/bin/python3
"""
Python module to run flask server
"""
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    return "HBNB"


@app.route('/c/<text>')
def c_route(text):
    return "C " + text.replace('_', ' ')


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_route(text):
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>')
def number_route(n):
    return f"{n} is a number"


@app.route('/number_template/<int:n>')
def number_template_route(n):
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
