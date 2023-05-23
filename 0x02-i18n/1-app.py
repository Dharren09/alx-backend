#!/usr/bin/env python3
"""instantiates the babel object, stores it in a module level variable
created a config class to set Babels default locale"""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """config class to configure available langs in our app,
    and set babels default locale"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """renders the template"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
