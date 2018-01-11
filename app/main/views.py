from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import User
from .. import db
from flask_login import login_user, logout_user, login_required, current_user
from ..email import mail_message
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from dateutil import rrule
from TwitterAPI import TwitterAPI
import json
from flask_dance.contrib.twitter import make_twitter_blueprint, twitter
import time
from time import mktime




@main.route('/')
def index():
    """View root page function that returns index page and the various news sources"""

    title = 'Home- Welcome to Twitfluence'

    return render_template('index.html', title=title)


@main.route('/twitter', methods = ['GET', 'POST'])
def twitter():
    """View route for loggin in with twitter"""

    if current_user.is_authenticated == False:
        return redirect(url_for("twitter.login"))
    resp = twitter.get("account/settings.json")
    assert resp.ok

    return render_template('search.html')



@main.route('/search', methods=['GET', 'POST'])
def search_user():
    consumer_key ='Zy6Ty56VKSCIZH2EjO4jaGMLo'
    consumer_secret ='8jeO4iShJyJMtkOt33iK8fo09n3EePa7mjxwyDVpKv9axYPdmq'
    access_token='300098394-Ip8cNXKnD6bsaXFSbPXwhsFWrKDvo9gQdXkuhNcK'
    access_token_secret='OQtSOnKHxIf0UpACvrCsKazWBYdFCP4dCXZqnjoJXxPF6'
    api = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)

    user_name = request.args.get('screen_name')

    payload={'screen_name':user_name}
    payload1={'screen_name':user_name, 'count':20}

    r = api.request('users/show', params=payload)
    f = api.request('statuses/user_timeline', params=payload1)

    info = r.json()
    info1 = f.json()

    date_created = time.strptime(info['created_at'], '%a %b %d %H:%M:%S %z %Y')
    dt = datetime.fromtimestamp(mktime(date_created)).date()
    print(dt)

    trends = api.request('trends/place', 'id=23424863')
    trends_info = trends.json()

    return render_template('search.html', info=info, info1=info1, trends_info=trends_info)
