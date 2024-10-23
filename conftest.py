import pytest
import requests
from src.data import Urls
from src.helpers import CreateRandomUser


@pytest.fixture
def create_user():
    user_data = CreateRandomUser.random_user()
    yield user_data
    login_user = requests.post(f'{Urls.BASE_URL}{Urls.LOG_IN}', data=user_data)
    token = login_user.json()['accessToken']
    delete_user = requests.delete(f'{Urls.BASE_URL}{Urls.UPDATE_USER}', headers={'Authorization': token})


