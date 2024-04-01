import allure
import requests
from handlers import Handlers
from urls import Urls
from user_data import data_updated


class TestChangeUserData:

    @allure.title("Изменение данных пользователя с авторизацией")
    def test_change_data_user(self, get_token):
        response = requests.patch(Urls.MAIN_URL + Handlers.CHANGE_USER_DATA,
                                  headers={'Authorization': get_token}, data=data_updated)
        assert response.status_code == 200 and response.json()['user']['name'] == 'Test'

    @allure.title("Изменение данных пользователя без авторизации")
    def test_change_user_fail(self):
        response = requests.patch(Urls.MAIN_URL + Handlers.CHANGE_USER_DATA,
                                  headers=Handlers.headers, data=data_updated)
        assert response.status_code == 400 and 'Bad Request' in response.text
