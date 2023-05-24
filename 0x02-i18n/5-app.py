#!/usr/bin/env python3
"""Basic Babel Flask extension,
instantiates the babel object in th app the stores it in module-level
variable"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
from datetime import datetime


app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """config class that configures the available langs in our app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def get_user():
    """Returns a user dictionary or None if the Id not found"""
    id = request.args.get("login_as")
    if id and int(id) in users:
        return users[int(id)]
    return None


@app.before_request
def before_request():
    """sets the user as global"""
    g.user = get_user()


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """Basic Flask app"""
    return render_template('5-index.html')


@babel.localeselector
def get_locale():
    """function determines appopriate lang basing on the
    users preference"""
    local = request.args.get("locale")
    if local and local in app.config["LANGUAGES"]:
        return local
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# babel.init_app(app, locale_selector=get_locale)

if __name__ == '__main__':
    app.run()
