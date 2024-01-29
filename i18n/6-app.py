#!/usr/bin/env python3
""" Create a basic Flask App
    with a single '/' route and an index.html template
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, refresh

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """ Configure available languages in our app """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
# Use Config class as config for our app
app.config.from_object(Config)


# Instantiate Babel object in module-level variable babel
babel = Babel(app)


def get_user():
    """ Return user dict if exists """
    user_id = request.args.get('login_as')
    if user_id:
        try:
            user_id = int(user_id)
            return users.get(user_id)
        except ValueError:
            # In case user_id is not an integer
            return None
    return None


# @babel.localeselector
def get_locale():
    """ Return user preferred locale, if not available return best match """
    # First priority: user locale from URL parameters
    url_locale = request.args.get('locale')
    if url_locale and url_locale in app.config['LANGUAGES']:
        return url_locale
    # Second priority: user locale from user settings
    if g.get('user'):
        user_locale = g.user.get('locale')
        if user_locale in app.config['LANGUAGES']:
            return user_locale
    # Third priority: user locale from request header
    return request.accept_languages.best_match(app.config['LANGUAGES'])
    # Fourth priority: default locale
    # return app.config['BABEL_DEFAULT_LOCALE'] # default locale


# babel.init_app(app, locale_selector=get_locale)


@app.before_request
def before_request():
    """ Set/get current user and
    current language from request parameters
    and refresh babel translations """
    g.user = get_user()

    g.locale = get_locale()

    refresh()


@app.route('/')
def index():
    """ Return index.html template """
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(debug=True)
