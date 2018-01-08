from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_mail import Mail
from flask_moment import Moment
from flask_dance.contrib.twitter import make_twitter_blueprint, twitter



bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
photos = UploadSet('photos', IMAGES)
mail = Mail()
moment = Moment()
blueprint = make_twitter_blueprint(
    api_key="xHeaXMvVSq1QmiyTZZnImAnbl",
    api_secret="EHSaXjfnokTkGMRiH4BydhOygJjo97tHBCVOxDHx9yG1Ki7Iu2",
)


def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations.
    app.config.from_object(config_options[config_name])

    # Intitializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    moment.init_app(app)
    login_manager.session_protection = 'strong'
    login_manager.login_view = 'auth.login'
    # configure upload setUp
    configure_uploads(app, photos)
    mail.init_app(app)
    # Registering the blueprint

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/authenticate')

    app.register_blueprint(blueprint, url_prefix="/login")

    return app
