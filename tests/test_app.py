import json
from .conftest import MOCKED_RESPONSE

# pylint: disable=unused-argument
def test_get_taxis(client, mock_response):
    response = client.get('/api/taxis/')
    response_data = json.loads(response.get_data(as_text=True))
    assert response_data['count'] == 3
    assert response_data['taxis'] == MOCKED_RESPONSE
