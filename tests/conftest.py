import sys

sys.path.append("..")

import os
import pytest
import logging

from models import Taxis

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app import create_app

MOCKED_RESPONSE = [
    {"id": "7249", "plate": "CNCJ-2997"},
    {
        "id": "10133",
        "plate": "PAOF-6727",
    },
    {
        "id": "2210",
        "plate": "FGMG-3071",
    },
]


@pytest.fixture
def app():
    """Create application for the tests."""
    _app = create_app()

    _app.config["TESTING"] = True
    _app.testing = True
    yield _app


@pytest.fixture
def client(app):
    client = app.test_client()
    yield client


class TaxiModelMock:
    # mock json() method always returns a specific testing dictionary
    @staticmethod
    def get_taxis():
        return MOCKED_RESPONSE


class MockResponse:
    @staticmethod
    def json():
        return {"mock_key": "mock_response"}


@pytest.fixture
def mock_response(monkeypatch):
    """Requests.get() mocked to return {'mock_key':'mock_response'}."""

    def mock_get(*args, **kwargs):
        return TaxiModelMock().get_taxis()

    monkeypatch.setattr(Taxis.TaxiModel, "get_taxis", mock_get)
