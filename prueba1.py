import json
import facebook
import requests
import re
from pyfacebook import Api

api = Api(app_id="your app id", app_secret="your app secret", application_only_auth=True)
api.get_token_info()
AccessToken(app_id='id', application='app name', user_id=None)
