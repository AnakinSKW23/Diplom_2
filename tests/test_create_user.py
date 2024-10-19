import allure
import pytest
import requests
from src.data import Urls, ServerAnswers
from src.helpers import CreateRandomUser, RealUserData, RandomUserWithoutFields

@allure.suite('Тестируем создание пользователя')
class TestCreateUser:

    @allure.title('Проверяем создание уникального пользователя')
    def test_create_user(self):
        user_data = CreateRandomUser.random_user()
        response = requests.post(f"{Urls.BASE_URL}{Urls.CREATE}", data=user_data)
        assert response.json()['success'] is True

    @allure.title('Проверяем создание пользователя, который уже зарегистрирован')
    def test_create_registrated_user(self):
        user_data = RealUserData.registrated_user()
        response = requests.post(f"{Urls.BASE_URL}{Urls.CREATE}", data=user_data)
        assert 403 == response.status_code and response.json()['message'] == ServerAnswers.registrated_user

    @allure.title('Проверяем создание пользователя при не заполненом обязательном поле: без почты, без пароля, без имени')
    @pytest.mark.parametrize('user_data',
                             [
                                 (RandomUserWithoutFields.user_without_email),
                                 (RandomUserWithoutFields.user_without_password),
                                 (RandomUserWithoutFields.user_without_name)
                             ]
                            )
    def test_create_user_without_any_fields(self, user_data):
        response = requests.post(f"{Urls.BASE_URL}{Urls.CREATE}", data=user_data)
        assert 403 == response.status_code and response.json()['message'] == ServerAnswers.empty_any_fields

