from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    bio = db.Column(db.String(255))
    location = db.Column(db.String(255))
    member_since = db.Column(db.DateTime(), default=datetime.utcnow)
    last_seen = db.Column(db.DateTime(), default=datetime.utcnow)
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'


class TwitterRequest:
    """search class to define search Objects"""

    def __init__(self, id, name,description, profile_image_url_https, statuses_count, followers_count, favourited_count, list_count):
        self.id = id
        self.name = name
        self.description = description
        self.profile_image_url_https = profile_image_url_https
        self.statuses_count = statuses_count
        self.followers_count = followers_count
        self.favourited_count = favourited_count
        self.list_count = list_count
