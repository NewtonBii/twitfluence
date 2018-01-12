from flask import render_template, redirect, url_for, flash
from . import twitter
from .. import db
from flask_dance.contrib.twitter import twitter, make_twitter_blueprint


@twitter.route('/twitter/authorized')
def login():
    if not twitter.authorized:
        return redirect(url_for('twitter.login'))
    resp = twitter.get("account/settings.json")
    assert resp.ok

    return render_template('search.html')
