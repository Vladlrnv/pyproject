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
        transaction_list = []
        csv_logger.info("Указан корректный путь. Список транзакций получен")
        csv_data = pd.read_csv(csv_file_path, delimiter=";")
        len_, b = csv_data.shape
        for i in range(len_):
            if csv_data["id"][i]:
                transaction_list.append(
                    {
                        "id": str(csv_data["id"][i]),
                        "state": csv_data["state"][i],
                        "date": csv_data["date"][i],
                        "operationAmount": {
                            "amount": str(csv_data["amount"][i]),
                            "currency": {
                                "name": csv_data["currency_name"][i],
                                "code": csv_data["currency_code"][i],
                            },
                        },
                        "description": csv_data["description"][i],
                        "from": csv_data["from"][i],
                        "to": csv_data["to"][i],
                    }
                )
    except Exception as e:
        csv_logger.warning(f"Ошибка: {e}.")
        return []
    return transaction_list


path = os.path.join(os.path.dirname(__file__), "..", "data", "transactions.csv")
# print(get_transactions_csv(path))


def get_transactions_excel(excel_file_path: Any) -> Any:
    """Функция возвращает список словарей, содержащий транзакции из файла transactions_excel.xlsx"""
    excel_logger.info("Начало работы программы")
    transaction_list = []
    try:
        excel_logger.info("Указан корректный путь. Список транзакций получен")
        excel_data = pd.read_excel(excel_file_path)
        len_, b = excel_data.shape
        for i in range(len_):
            if excel_data["id"][i]:
                transaction_list.append(
                    {
                        "id": str(excel_data["id"][i]),
                        "state": excel_data["state"][i],
                        "date": excel_data["date"][i],
                        "operationAmount": {
                            "amount": str(excel_data["amount"][i]),
                            "currency": {
                                "name": excel_data["currency_name"][i],
                                "code": excel_data["currency_code"][i],
                            },
                        },
                        "description": excel_data["description"][i],
                        "from": excel_data["from"][i],
                        "to": excel_data["to"][i],
                    }
                )
            else:
                continue
    except Exception as r:
        excel_logger.warning(f"Ошибка: {r}.")
        return []
    return excel_data


path_to_excel = os.path.join(os.path.dirname(__file__), "..", "data", "transactions_excel.xlsx")
# print(get_transactions_excel(path_to_excel))
