#!/usr/bin/env python3
""" Create a basic Flask App

    with a single '/' route and an index.html template
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """ Return index.html template """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
