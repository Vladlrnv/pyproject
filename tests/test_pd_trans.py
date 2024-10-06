from typing import Any
from unittest.mock import patch

import pandas as df
from coverage.annotate import os

from src.pd_trans import get_transactions_csv, get_transactions_excel


@patch("src.pd_trans.pd.read_csv")
def test_get_transactions_csv(mock_read: Any, df_csv_transaction: df.DataFrame) -> Any:
    mock_read.return_value = df_csv_transaction
    result = get_transactions_csv(os.path.join(os.path.dirname(__file__), "..", "data", "transactions.csv"))
    expected = df_csv_transaction.to_dict(orient="records")
    assert result == expected


def test_get_transactions_csv_empty() -> Any:
    assert get_transactions_csv("some_text") == []


@patch("src.pd_trans.pd.read_excel")
def test_get_transactions_excel(mock_read: Any, df_csv_transaction: df.DataFrame) -> Any:
    mock_read.return_value = df_csv_transaction
    result = get_transactions_excel(os.path.join(os.path.dirname(__file__), "..", "data", "transactions_excel.xlsx"))
    expected = df_csv_transaction.to_dict(orient="records")
    assert result == expected


def test_get_transactions_excel_empty() -> Any:
    assert get_transactions_excel("some_text") == []
