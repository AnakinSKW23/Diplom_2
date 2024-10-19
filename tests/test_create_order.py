import allure
import requests
from src.data import Urls, Ingredients, ServerAnswers
from src.helpers import CreateRandomUser

@allure.suite('Тестируем создание заказа')
class TestCreateOrder:

    @allure.title('Проверяем создание заказа с авторизацией')
    def test_create_order_autorized_user(self):
        user_data = CreateRandomUser.random_user()
        response = requests.post(f"{Urls.BASE_URL}{Urls.CREATE}", data=user_data)
        get_token = response.json()['accessToken']
        data = {'ingredients': [Ingredients.BUN_R2_D3, Ingredients.SAUSE_SPICY_X]}
        create_order = requests.post(f"{Urls.BASE_URL}{Urls.CREATE_ORDER}", data=data, headers={
            'Authorization': f'{get_token}'})
        assert create_order.json()['success'] is True

    @allure.title('Проверяем создание заказа без авторизации')
    def test_create_order_unautorized_user(self):
        user_data = CreateRandomUser.random_user()
        response = requests.post(f"{Urls.BASE_URL}{Urls.CREATE}", data=user_data)
        data = {'ingredients': [Ingredients.BUN_R2_D3, Ingredients.SAUSE_SPICY_X]}
        create_order = requests.post(f"{Urls.BASE_URL}{Urls.CREATE_ORDER}", data=data)
        assert create_order.json()['success'] is True

    @allure.title('Проверяем создание заказа с неверным хешем ингредиентов')
    def test_create_wrong_ingredient(self):
        user_data = CreateRandomUser.random_user()
        response = requests.post(f"{Urls.BASE_URL}{Urls.CREATE}", data=user_data)
        data = {'ingredients': [Ingredients.BUN_SHAO_KAN]}
        create_order = requests.post(f"{Urls.BASE_URL}{Urls.CREATE_ORDER}", data=data)
        assert 500 == create_order.status_code

    @allure.title('Проверяем создание заказа без ингредиентов')
    def test_create_withot_ingredient(self):
        user_data = CreateRandomUser.random_user()
        response = requests.post(f"{Urls.BASE_URL}{Urls.CREATE}", data=user_data)
        data = {'ingredients': ['']}
        create_order = requests.post(f"{Urls.BASE_URL}{Urls.CREATE_ORDER}", data=data)
        assert 400 == create_order.status_code and create_order.json()['message'] == ServerAnswers.no_ingredient


