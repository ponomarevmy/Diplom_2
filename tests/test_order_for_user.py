import allure
import requests
from handlers import Handlers
from urls import Urls
from user_data import data_updated


class TestGetOrderUser:

    @allure.story("Запрос на получение заказов авторизованного пользователя")
    def test_get_order_login_user(self, get_token):
        response = requests.get(Urls.MAIN_URL + Handlers.GET_ORDERS,
                                headers={'Authorization': get_token}, data=data_updated)
        body = response
        assert response.status_code == 200 and body.json()['success'] == True

    @allure.story("Запрос на получение заказов неавторизованного пользователя")
    def test_updated_order_not_login_user(self):
        response = requests.get(Urls.MAIN_URL + Handlers.GET_ORDERS, headers=Handlers.headers)
        body = response
        assert response.status_code == 401 and body.json()['success'] == False
