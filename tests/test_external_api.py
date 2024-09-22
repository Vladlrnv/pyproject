from unittest.mock import patch

from src.external_api import converter


@patch("requests.get")
def test_converter(mock_get, trans):
    mock_get.return_value.json.return_value = ({"result": 760604.53})
        # {
        #     "date": "2024-09-22",
        #     "info": {
        #         "rate": 92.515546,
        #         "timestamp": 1726982235
        #     },
        #     "query": {
        #         "amount": 8221.37,
        #         "from": "USD",
        #         "to": "RUB"
        #     },
        #     "result": 760604.534418,
        #     "success": True
        # }
    assert converter(trans) == 76064.53
