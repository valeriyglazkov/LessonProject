from faker import Faker
from app_driver.owf_http_client import OwfHttpClient
from config import APP_BASE_URL
from test_data.context import TestContext
from test_data.data_helper import bad_phone
from test_data.models.view_models import RegisterVm

faker = Faker('ru-RU')
client = OwfHttpClient(APP_BASE_URL)

SUCCESS_CREATE_USER = [
    TestContext.from_dict({
        "register": RegisterVm.from_dict({
            "email": faker.email(),
            "password": "Test123",
            "confirmPassword": "Test123",
            "lastName": faker.first_name(),
            "firstName": faker.last_name(),
            "patronymic": faker.first_name() + "ович",
            "phoneNumber": "+79999999999"
        })
    }),
    TestContext.from_dict({
        "register": RegisterVm.from_dict({
            "email": faker.email(),
            "password": "Test123",
            "confirmPassword": "Test123",
            "lastName": faker.first_name(),
            "firstName": faker.last_name(),
            "patronymic": "",
            "phoneNumber": "+79999999999"
        })
    })
]

NO_EMAIL = {
    "password": "Test123",
    "confirmPassword": "Test123",
    "lastName": faker.first_name(),
    "firstName": faker.last_name(),
    "patronymic": faker.first_name() + "ович",
    "phoneNumber": "+79999999999"
}

NO_PASSWORD = {
    "email": faker.email(),
    "confirmPassword": "Test123",
    "lastName": faker.first_name(),
    "firstName": faker.last_name(),
    "patronymic": faker.first_name() + "ович",
    "phoneNumber": "+79999999999"
}

PASSWORDS_DONT_MATCH = {
    "email": faker.email(),
    "password": "Test123",
    "confirmPassword": "Test1231",
    "lastName": faker.first_name(),
    "firstName": faker.last_name(),
    "patronymic": faker.first_name() + "ович",
    "phoneNumber": "+79999999999"
}

ALREADY_REGISTERED = {
    "email": "astrallkptest@gmail.com",
    "password": "Test123",
    "confirmPassword": "Test123",
    "lastName": faker.first_name(),
    "firstName": faker.last_name(),
    "patronymic": faker.first_name() + "ович",
    "phoneNumber": "+79999999999"
}

BAD_PHONE = [
    TestContext.from_dict({
        "badPhone": RegisterVm.from_dict(bad_phone("+7-999-999-99-99"))
    }),
    TestContext.from_dict({
        "badPhone": RegisterVm.from_dict(bad_phone("+34999999999"))
    }),
    TestContext.from_dict({
        "badPhone": RegisterVm.from_dict(bad_phone("99999999"))
    }),
    TestContext.from_dict({
        "badPhone": RegisterVm.from_dict(bad_phone("89999999999"))
    })
]
