# -*- coding: utf-8 -*-
import logging
import os.path
from typing import Any

import pandas as pd

csv_logger = logging.getLogger("get_transactions_csv")
file_handler = logging.FileHandler(r"C:\Users\ADMIN\PycharmProjects\pythonProject3\logs\logs.log", "w")
file_formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
file_handler.setFormatter(file_formatter)
csv_logger.addHandler(file_handler)
csv_logger.setLevel(logging.DEBUG)
excel_logger = logging.getLogger("get_transactions_excel")
excel_logger.addHandler(file_handler)
excel_logger.setLevel(logging.DEBUG)


def get_transactions_csv(csv_file_path: Any) -> Any:
    """Функция возвращает список словарей, содержащий транзакции из файла transactions.csv"""
    csv_logger.info("Начало работы программы")
    try:
        csv_logger.info("Указан корректный путь. Список транзакций получен")
        csv_data = pd.read_csv(csv_file_path)
        df_csv_data = csv_data.to_dict(orient="records")
        return df_csv_data
    except FileNotFoundError as e:
        csv_logger.warning(f"Ошибка: {e}. Указан неверный путь")
        return []


path = os.path.join(os.path.dirname(__file__), "..", "data", "transactions.csv")
print(get_transactions_csv(path))


def get_transactions_excel(excel_file_path: Any) -> Any:
    """Функция возвращает список словарей, содержащий транзакции из файла transactions_excel.xlsx"""
    excel_logger.info("Начало работы программы")
    try:
        excel_data = pd.read_excel(excel_file_path)
        df_excel_data = excel_data.to_dict(orient="records")
        excel_logger.info("Указан корректный путь. Список транзакций получен")
        return df_excel_data
    except FileNotFoundError as r:
        csv_logger.warning(f"Ошибка: {r}. Указан неверный путь")
        return []


path_to_excel = os.path.join(os.path.dirname(__file__), "..", "data", "transactions_excel.xlsx")
print(get_transactions_excel(path_to_excel))
