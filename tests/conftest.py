import pytest

# import logging
from fleet_api.app import create_app
from fleet_api.models import taxis
from .mock_data import TAXIS_RESPONSE

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


# def get_taxis(_page, _per_page):
#     return TAXIS_RESPONSE

# @pytest.fixture
# def _get_mock_response(monkeypatch):
#     monkeypatch.setattr(taxis, "get", get_taxis)
