from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import User
from .. import db
from flask_login import login_user, logout_user, login_required, current_user
from ..email import mail_message
from datetime import datetime
from TwitterAPI import TwitterAPI
from twitter import *
import json



@main.route('/', methods = ['GET', 'POST'])
def index():
    """View root page function that returns index page and the various news sources"""

    title = 'Home- Welcome to Twitfluence'

    return render_template('index.html', title=title)

@main.route('/user', methods = ['GET', 'POST'])
def user():
    api = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)
    r = api.request('users/show', {'screen_name':'BiiNewton'})
    info = r.json()
    return render_template('twitter.html')

@main.route('user/search/<screen_name>', methods=['GET', 'POST'])
def search_user(screen_name):
