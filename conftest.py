from collections import defaultdict
import psycopg2
import pytest
from config import DB_CONNECTION_PARAMS, APP_BASE_URL
from app_driver.owf_http_client import OwfHttpClient
from app_driver.db_cleaner import DBCleaner
from app_driver.user_repository import UserRepository


@pytest.fixture(scope='session')
def http_client():
    return OwfHttpClient(APP_BASE_URL)


@pytest.fixture(scope='session')
def db_connection():
    connection = psycopg2.connect(
        dbname=DB_CONNECTION_PARAMS.get('dbname'),
        user=DB_CONNECTION_PARAMS.get('user'),
        password=DB_CONNECTION_PARAMS.get('password'),
        host=DB_CONNECTION_PARAMS.get('host')
    )

    yield UserRepository(connection)

    connection.close()


@pytest.fixture(scope='session')
def user_repository(db_connection):
    return UserRepository(db_connection)


@pytest.fixture(scope='session')
def clear_users(db_connection):
    yield
    cleaner = DBCleaner(db_connection)
    cleaner.delete_users()


__TEST_FAILED_INCREMENTAL = defaultdict(dict)


def pytest_runtest_makereport(item, call):
    if "incremental" in item.keywords:
        if call.excinfo is not None and call.excinfo.typename != "Skipped":
            param = tuple(item.callspec.indices.values()) if hasattr(item, "callspec") else ()
            __TEST_FAILED_INCREMENTAL[str(item.cls)].setdefault(param, item.originalname or item.name)


def pytest_runtest_setup(item):
    if "incremental" in item.keywords:
        param = tuple(item.callspec.indices.values()) if hasattr(item, "callspec") else ()
        originalname = __TEST_FAILED_INCREMENTAL[str(item.cls)].get(param)
        if originalname:
            pytest.xfail("previous test failed ({})".format(originalname))