import json
import allure
import requests
from handlers import Handlers
from urls import Urls
from user_data import data_correct, data_updated


class TestChangeUserData:
    @allure.step("Получение токена для авторизации")
    def get_token(self):
        token = requests.post(Urls.MAIN_URL + Handlers.LOGIN, headers=Handlers.headers,
                              data=json.dumps(data_correct))
        new_token = token.json()['accessToken']
        return new_token

    @allure.title("Изменение данных пользователя с авторизацией")
    def test_change_data_user(self):
        new_token = self.get_token()
        response = requests.patch(Urls.MAIN_URL + Handlers.CHANGE_USER_DATA,
                                  headers={'Authorization': new_token}, data=data_updated)
        assert response.status_code == 200 and response.json()['user']['name'] == 'Test'

    @allure.title("Изменение данных пользователя без авторизации")
    def test_create_user_fail(self):
        response = requests.patch(Urls.MAIN_URL + Handlers.CHANGE_USER_DATA,
                                  headers=Handlers.headers, data=data_updated)
        assert response.status_code == 400