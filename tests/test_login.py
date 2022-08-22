from config import APP_BASE_URL
from test_data.login_user import LOGIN
from app_driver.owf_http_client import OwfHttpClient


class TestSuccessCreateUser:

    def setup(self):
        self.client = OwfHttpClient(APP_BASE_URL)

    def test_login(self):
        login_response = self.client.login(LOGIN)
        response_body = login_response.json()
        assert login_response.status_code == 200
        assert response_body["accessToken"] is not None
        assert response_body["expiration"] is not None
