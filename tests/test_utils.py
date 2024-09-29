from typing import Any
from unittest.mock import patch, mock_open

from src.utils import get_transactions


@patch("os.path.exists")
@patch("json.load")
def test_get_transactions_valid_json(mocked_load, mock_os_path_exists):
    mock_os_path_exists.return_value = True
    m = mock_open()
    with patch("builtins.open", m) as mocked_open:
        mocked_load.return_value = [
            {"amount": "100", "currency": "RUB"},
            {"amount": "200", "currency": "USD"},
        ]
        assert get_transactions("operations.json") == [
            {"amount": "100", "currency": "RUB"},
            {"amount": "200", "currency": "USD"},
        ]
        mocked_open.assert_called_with("operations.json", "r",
                                       encoding="utf-8")


def test_get_transactions_empty() -> Any:
    assert get_transactions("some_text") == []
