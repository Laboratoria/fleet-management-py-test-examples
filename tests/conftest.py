import pytest
import dotenv

# import logging
from fleet_api.app import create_app
from fleet_api.config import TestConfig

# dir structure of python tests
# https://flask.palletsprojects.com/en/3.0.x/testing/
# https://flask.palletsprojects.com/en/3.0.x/tutorial/tests/#setup-and-fixtures
@pytest.fixture
def app():
    """Create application for the tests."""
    dotenv.load_dotenv()
    config = TestConfig()
    _app = create_app(config)

    _app.config["TESTING"] = True
    _app.testing = True
    yield _app

@pytest.fixture
# pylint: disable=redefined-outer-name
def client(app):
    client = app.test_client()
    yield client

