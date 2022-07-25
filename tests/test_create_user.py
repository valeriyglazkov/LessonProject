import psycopg2
from config import APP_BASE_URL, DB_CONNECTION_PARAMS
from test_data.create_user import SCENARIO
from app_driver.owf_http_client import OwfHttpClient
from app_driver.user_repository import UserRepository


class TestUserCreatedSuccessfully:
    """Успешное создание нового юзера"""

    def setup(self):
        """Установка соединения с БД"""
        self.client = OwfHttpClient(APP_BASE_URL)
        self.connection = psycopg2.connect(
            dbname=DB_CONNECTION_PARAMS.get('dbname'),
            user=DB_CONNECTION_PARAMS.get('user'),
            password=DB_CONNECTION_PARAMS.get('password'),
            host=DB_CONNECTION_PARAMS.get('host')
        )
        self.user_repository = UserRepository(self.connection)

    def test_register(self):
        """Регистрация нового юзера"""
        register_response = self.client.register(SCENARIO)
        assert register_response.status_code == 200

    def test_login(self):
        """Авторизация и получение токена доступа"""
        login_data = {
            'email': SCENARIO['email'],
            'password': SCENARIO['password']
        }

        login_response = self.client.login(login_data)

        assert login_response.status_code == 200

    def test_get_user_data(self):
        self.user_repository.get_users()
        # print(self.user_repository.get_user_id())

    # def delete_user(self):
    #     self.user_repository.delete_user()

    def teardown(self):
        self.connection.close()
