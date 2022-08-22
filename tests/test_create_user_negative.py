import pytest

from app_driver.db_cleaner import DBCleaner
from config import APP_BASE_URL, DB_CONNECTION_PARAMS
from test_data.context import TestContext
from test_data.create_user import NO_EMAIL, NO_PASSWORD, ALREADY_REGISTERED, BAD_PHONE, PASSWORDS_DONT_MATCH
from app_driver.owf_http_client import OwfHttpClient
from test_data.models.view_models import RegisterVm


class TestNoSuccessCreateUser:

    def setup(self):
        self.http_client = OwfHttpClient(APP_BASE_URL)
        self.db_cleaner = DBCleaner(DB_CONNECTION_PARAMS)
        self.db_cleaner.delete_users()
        self.http_client.register_bad_requests(ALREADY_REGISTERED)

    def test_register_no_email(self):
        register_response = self.http_client.register_bad_requests(NO_EMAIL)
        response_body = register_response.json()
        assert register_response.status_code == 400
        assert response_body["errors"]["Email"] == ["The Email field is required."]

    def test_register_no_password(self):
        register_response = self.http_client.register_bad_requests(NO_PASSWORD)
        response_body = register_response.json()
        assert register_response.status_code == 400
        assert response_body["errors"]["Password"] == ["The Password field is required."]

    def test_password_dont_match(self):
        register_response = self.http_client.register_bad_requests(PASSWORDS_DONT_MATCH)
        response_body = register_response.json()
        assert register_response.status_code == 400
        assert response_body["errorMessage"] == "Пароли не совпадают"

    def test_register_already_registered(self):
        register_response = self.http_client.register_bad_requests(ALREADY_REGISTERED)
        response_body = register_response.json()
        assert register_response.status_code == 400
        assert response_body["errorMessage"] == "Пользователь с Email: " + ALREADY_REGISTERED[
            'email'] + " уже зарегистрирован"

    @pytest.mark.incremental
    @pytest.mark.parametrize('test_data', BAD_PHONE, scope="class")
    def test_register_bad_phone(self, test_data: TestContext):
        register_data: RegisterVm = test_data.get('badPhone')
        response = self.http_client.register(register_data)
        test_data = response.json()
        assert response.status_code == 400
        assert test_data["errorMessage"] == "Номер телефона должен соответствовать регулярному выражению ^\\+7\\d{10}$"
