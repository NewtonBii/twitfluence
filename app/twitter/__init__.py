from flask_dance.contrib.twitter import make_twitter_blueprint, twitter
twitter = make_twitter_blueprint('twitter', __name__, api_key="dWsKFkfCXTKo42qbtEacqDJsj",api_secret="HVkYw19eMvmjnWmUPElPyLHQrrUJLfoDSMAjBL7MCDqs2wj1OX")
from . import views
