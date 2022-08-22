import pytest

from app_driver.db_cleaner import DBCleaner
from app_driver.db_connection import DbConnector
from config import APP_BASE_URL, DB_CONNECTION_PARAMS
from test_data.context import TestContext
from test_data.create_user import SUCCESS_CREATE_USER
from test_data.data_helper import assert_login_getAdmin
from app_driver.owf_http_client import OwfHttpClient
from test_data.models.view_models import *


@pytest.mark.incremental
@pytest.mark.parametrize('test_data', SUCCESS_CREATE_USER, scope="class")
class TestSuccessCreateUser:

    def setup_class(self):
        self.http_client = OwfHttpClient(APP_BASE_URL)
        self.db_connector = DbConnector(DB_CONNECTION_PARAMS)
        self.db_cleaner = DBCleaner(DB_CONNECTION_PARAMS)

    def test_success_register(self, test_data: TestContext):
        # Arrange
        register_data: RegisterVm = test_data.get('register')

        # Act
        response = self.http_client.register(register_data)

        # Assert
        test_data = response.json()
        assert response.status_code == 200
        assert test_data["message"] == "Пользователь " + register_data.email + " успешно зарегистрирован"
        assert_login_getAdmin(self, register_data.email)

    def teardown_class(self):
        self.db_cleaner.delete_users()
