import json
import pytest
import requests
from handlers import Handlers
from urls import Urls
from user_data import data_correct


@pytest.fixture(scope='function')
def get_token():
    token = requests.post(Urls.MAIN_URL + Handlers.LOGIN, headers=Handlers.headers,
                          data=json.dumps(data_correct))
    new_token = token.json()['accessToken']
    return new_token
