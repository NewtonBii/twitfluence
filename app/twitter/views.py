from flask import render_template, redirect, url_for, flash
from . import blueprint
from .. import db
from flask_dance.contrib.twitter import twitter

@blueprint.route('/twitter/authorized')
def twitter_login():
    if not twitter.authorized:
        return redirect(url_for('twitter.login'))
    resp = twitter.get("account/settings.json")
    assert resp.ok
    response = resp.json()
    return render_template('twitter.html', response=response)
