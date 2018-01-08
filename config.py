import os

class Config:

    TWITTER_API_BASE_URL = 'https://api.twitter.com/1.1/users/lookup.json?screen_name=twitterapi,twitter/{}?api_key={}'
    TWITTER_API_KEY = ''
    SECRET_KEY =   'kepha'

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://rkepha:KR@localhost/twitfluenceKT'


class ProdConfig(Config):
    pass




class DevConfig(Config):
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
