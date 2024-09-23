from typing import Any
from unittest.mock import patch

from src.external_api import converter


@patch("requests.get")
def test_converter(mock_get: Any, trans: Any) -> Any:
    mock_get.return_value.status_code = 200
    mock_get.return_value.ok = True
    mock_get.return_value.json.return_value = {"result": 760604.53}
    assert converter(trans) == 760604.53
    mock_get.assert_called_once()


def test_converter_rub(trans_2: Any) -> Any:
    assert converter(trans_2) == "8221.37"
