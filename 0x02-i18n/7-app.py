#!/usr/bin/env python3
"""Basic Babel Flask extension,
instantiates the babel object in th app the stores it in module-level
variable"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from datetime import datetime
import pytz


app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
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
    return render_template('7-index.html')


@babel.localeselector
def get_locale():
    local = request.args.get("locale")
    if local and local in app.config["LANGUAGES"]:
        return local
    if get_user():
        local = get_user()["locale"]
        if local and local in app.config["LANGUAGES"]:
            return local
    local = request.headers.get("locale")
    if local and local in app.config["LANGUAGES"]:
        return local
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """Retrieve time zone"""
    tz = request.args.get("timezone")
    try:
        pytz.timezone(tz)
        return tz
    except pytz.exceptions.UnknownTimeZoneError:
        pass
    if g.user:
        tz = g.user["timezone"]
        try:
            pytz.timezone(tz)
            return tz
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    return pytz.timezone(app.config["BABEL_DEFAULT_TIMEZONE"])


# babel.init_app(app, locale_selector=get_locale)

if __name__ == '__main__':
    app.run()
