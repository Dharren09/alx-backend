#!/usr/bin/env python3
"""basic flask app that creates a single route"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """Basic Flask app"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
