from typing import Any
from unittest.mock import patch

from src.utils import get_transactions


@patch("os.path.exists")
@patch("json.load")
def test_get_transaction_open(mocked_load: Any, mocked_os_path_exists: Any, utils: Any) -> Any:
    mocked_os_path_exists.return_value = True
    # m = mock_open()
    # with patch('builtins.open', m) as mocked_open:
    mocked_load.return_value = {"amount": "100", "currency": "RUB"}, {"amount": "200", "currency": "USD"}
    assert get_transactions(utils) == ({"amount": "100", "currency": "RUB"}, {"amount": "200", "currency": "USD"})


def test_get_transactions_empty() -> Any:
    assert get_transactions("some_text") == []
