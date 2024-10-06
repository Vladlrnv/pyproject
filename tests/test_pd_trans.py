# -*- coding: utf-8 -*-
# from typing import Any
# from unittest.mock import patch, mock_open
#
# import pandas as df
# import pandas as pd
#
# from src.pd_trans import get_transactions_csv, get_transactions_excel
#
#
# @patch("src.pd_trans.pd.read_csv")
# def test_get_transactions_csv(mock_read_csv: Any, df_csv_transaction: pd.DataFrame) -> Any:
#     mock_read_csv.return_value = df_csv_transaction
#     result = get_transactions_csv(r"C:\Users\ADMIN\PycharmProjects\pythonProject3\data\transactions_excel.xlsx")
#     expected = df_csv_transaction.to_dict(orient="records")
#     assert result == expected


# def test_get_transactions_csv_empty() -> Any:
#     assert get_transactions_csv("some_text") == []
#
#
# @patch("src.pd_trans.pd.read_excel")
# def test_get_transactions_excel(mock_read: Any, df_csv_transaction: df.DataFrame) -> Any:
#     mock_read.return_value = df_csv_transaction
#     result = get_transactions_excel(os.path.join(os.path.dirname(__file__), "..", "data", "transactions_excel.xlsx"))
#     expected = df_csv_transaction
#     assert result == expected
#
#
# def test_get_transactions_excel_empty() -> Any:
#     assert get_transactions_excel("some_text") == []
