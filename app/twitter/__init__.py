from flask_dance.contrib.twitter import make_twitter_blueprint, twitter

blueprint = make_twitter_blueprint(
    api_key="dWsKFkfCXTKo42qbtEacqDJsj",
    api_secret="HVkYw19eMvmjnWmUPElPyLHQrrUJLfoDSMAjBL7MCDqs2wj1OX",
)

from . import views
