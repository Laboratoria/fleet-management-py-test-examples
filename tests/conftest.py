import pytest

# import logging
from fleet_api.app import create_app

# dir structure of python tests
# https://flask.palletsprojects.com/en/3.0.x/testing/
# https://flask.palletsprojects.com/en/3.0.x/tutorial/tests/#setup-and-fixtures
@pytest.fixture
def app():
    """Create application for the tests."""
    _app = create_app()

    _app.config["TESTING"] = True
    _app.testing = True
    yield _app

@pytest.fixture
# pylint: disable=redefined-outer-name
def client(app):
    client = app.test_client()
    yield client

