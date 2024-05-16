import allure
import requests
from handlers import Handlers
from urls import Urls
from user_data import data_correct, data_negative


class TestLoginUser:
    @allure.title('Авторизация пользователя')
    def test_login_user(self):
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.LOGIN}', data=data_correct)
        assert response.status_code == 200 and response.json().get('success') == True

    @allure.title('Пользователь не может авторизоваться, если указаны не корректные учетные данные')
    def test_login_user_negative(self):
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.LOGIN}', data=data_negative)
        assert response.status_code == 401 and response.json().get('success') == False
