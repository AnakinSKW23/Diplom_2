import allure
import pytest
import requests
from src.data import Urls, ServerAnswers
from src.helpers import RealUserData, LogInUser

@allure.suite('Тестируем логин пользователя')
class TestLogInUser:

    @allure.title('Проверяем логин под существующим пользователем')
    def test_log_in_real_user(self):
        user_data = RealUserData.real_user_data()
        response = requests.post(f"{Urls.BASE_URL}{Urls.LOG_IN}", data=user_data)
        assert response.json()['success'] is True

    @allure.title('Проверяем логин под не существующим пользователем')
    @pytest.mark.parametrize('user_data',
                             [
                                 (LogInUser.log_in_wrong_email),
                                 (LogInUser.log_in_wrong_password)
                             ]
                            )
    def test_log_in_user_without_any_fields(self, user_data):
        response = requests.post(f"{Urls.BASE_URL}{Urls.LOG_IN}", data=user_data)
        assert 401 == response.status_code and response.json()['message'] == ServerAnswers.unautorized_user

