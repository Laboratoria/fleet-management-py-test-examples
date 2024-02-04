import pytest

# import logging
from fleet_api.app import create_app
from fleet_api.models import taxis

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

MOCK_LOCATIONS = [
    {
        "id": 6418,
        "plate": "GHGH-1458",
        "timestamp": 1202435486,
        "lat": 116.30509,
        "lon": 39.96563,
    },
    {
        "id": 6419,
        "plate": "GHGH-1458",
        "timestamp": 1202435486,
        "lat": 116.30509,
        "lon": 39.96563,
    },
    {
        "id": 6420,
        "plate": "GHGH-1458",
        "timestamp": 1202435486,
        "lat": 116.30509,
        "lon": 39.96563,
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
    # pylint: disable=redefined-outer-name
    client = app.test_client()
    yield client

# pylint: disable=unused-argument
def get_mock(page=1, per_page=10):
    return MOCKED_RESPONSE


@pytest.fixture
def mock_response(monkeypatch):
    monkeypatch.setattr(taxis, "get", get_mock)
