import allure
import pytest
import requests
from src.data import Urls, ServerAnswers
from src.helpers import CreateRandomUser

@allure.suite('Тестируем изменение данных пользователя')
class TestChangeUser:

    @allure.title('Проверяем изменение данных авторизованного пользователя')
    @pytest.mark.parametrize('update_data', [
                                             ({'email: faker.email()'}),
                                             ({'password: faker.password()'}),
                                             ({'name: faker.name()'})
                                            ]
                            )
    def test_change_autorized_user(self, update_data):
        user_data = CreateRandomUser.random_user()
        response = requests.post(f"{Urls.BASE_URL}{Urls.CREATE}", data=user_data)
        get_token = response.json()['accessToken']
        new_data = requests.patch(f"{Urls.BASE_URL}{Urls.UPDATE_USER}",
                                data=update_data, headers={'Authorization': f'{get_token}'})
        assert new_data.json()['success'] is True

    @allure.title('Проверяем изменение данных не авторизованного пользователя')
    @pytest.mark.parametrize('update_data', [
                                             ({'email: faker.email()'}),
                                             ({'password: faker.password()'}),
                                             ({'name: faker.name()'})
                                            ]
                             )
    def test_change_unautorized_user(self, update_data):
        user_data = CreateRandomUser.random_user()
        response = requests.post(f"{Urls.BASE_URL}{Urls.CREATE}", data=user_data)
        get_token = None
        new_data = requests.patch(f"{Urls.BASE_URL}{Urls.UPDATE_USER}",
                                  data=update_data, headers={'Authorization': f'{get_token}'})
        assert 401 == new_data.status_code and new_data.json()['message'] == ServerAnswers.no_token

