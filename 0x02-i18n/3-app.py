#!/usr/bin/env python3
"""Basic Babel Flask extension,
instantiates the babel object in th app the stores it in module-level
variable"""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """config class that configures the available langs in our app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """Basic Flask app"""
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# babel.init_app(app, locale_selector=get_locale)

if __name__ == '__main__':
    app.run()
