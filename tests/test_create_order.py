import allure
import requests
from urls import Urls
from handlers import Handlers
from user_data import data_ingredients, data_ingredients_bad, data_not_ingredients


class TestCreateOrder:

    @allure.title("Создания заказа без авторизации с ингредиентами")
    def test_create_order_true(self):
        response = requests.post(Urls.MAIN_URL + Handlers.MAKE_ORDER, headers=Handlers.headers, json=data_ingredients)
        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title("Создания заказа без авторизации без ингредиентов")
    def test_create_order_not_ingredients(self):
        response = requests.post(Urls.MAIN_URL + Handlers.MAKE_ORDER, headers=Handlers.headers,
                                 json=data_not_ingredients)
        assert response.status_code == 400 and response.json()["success"] is False

    @allure.title("Создания заказа без авторизации с неверным хешем ингредиентов")
    def test_create_order_bad_ingredients(self):
        response = requests.post(Urls.MAIN_URL + Handlers.MAKE_ORDER, headers=Handlers.headers,
                                 json=data_ingredients_bad)
        assert response.status_code == 500 and 'Internal Server Error' in response.text
