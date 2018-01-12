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
import math




@main.route('/')
def index():
    """View root page function that returns index page and the various news sources"""

    title = 'Home- Welcome to Twitfluence'

    return render_template('index.html', title=title)

# @main.route('/twitter/authorized')
# def twitter_login():
#     if not twitter.authorized:
#         return redirect(url_for('twitter.login'))
#     resp = twitter.get("account/settings.json")
#     assert resp.ok
#
#     return render_template('search.html')

@main.route('/search', methods=['GET', 'POST'])
def search_user():
    consumer_key ='AQiZnAVb1NlnMJooyIYonMiO8'
    consumer_secret ='l08BAtgpJjOnblfJYxOK5gip2XSbQCNhsg7vNj9zcgmdLg2t3J'
    access_token='300098394-Ip8cNXKnD6bsaXFSbPXwhsFWrKDvo9gQdXkuhNcK'
    access_token_secret='OQtSOnKHxIf0UpACvrCsKazWBYdFCP4dCXZqnjoJXxPF6'
    api = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)

    user_name = request.args.get('screen_name')

    if user_name is None:
        user_name = 'twitterdev'
    payload={'screen_name':user_name}
    r = api.request('users/lookup', params=payload)
    info = r.json()[0]

    date_created = info['created_at']
    date_created_time_struct = time.strptime(date_created, '%a %b %d %H:%M:%S %z %Y')
    date_created_date = datetime.fromtimestamp(mktime(date_created_time_struct)).date()
    date_now=datetime.now().date()
    delta = date_now - date_created_date
    number_of_days = delta.days
    number_of_tweets = info['statuses_count']
    number_of_followers = info['followers_count']
    number_of_following = info['friends_count']

    def twitfluence(tweets, days, followers, following):
        first=math.log((tweets/days)*followers*(math.log(((followers/following)+1),10)), 10)
        if first > 10:
            return 10
        if first < 0:
            return 0.1
        return first

    twitfluence_score = twitfluence(number_of_tweets,number_of_days, number_of_followers, number_of_following)
    percentage_score = math.floor(twitfluence_score*10)

    trends = api.request('trends/place', 'id=1528488').json()[0]['trends']

    print(trends[0])


    return render_template('search.html', info=info, percentage_score=percentage_score, trends =trends)
