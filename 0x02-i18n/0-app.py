#!/usr/bin/env python3
"""basic flask app that creates a single route"""

from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
