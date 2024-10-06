import json
import logging
import os.path
from typing import Any

transactions_logger = logging.getLogger("get_transactions")
file_handler = logging.FileHandler(r"C:\Users\ADMIN\PycharmProjects\pythonProject3\logs\logs.log", "w")
file_formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
file_handler.setFormatter(file_formatter)
transactions_logger.addHandler(file_handler)
transactions_logger.setLevel(logging.INFO)


def get_transactions(file_path: Any) -> Any:
    """Функция возвращает список словарей с данными о финансовых транзакциях"""
    transactions_logger.info("Начало работы программы")
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            transactions_logger.info("Путь указан корректно. Список транзакций получен")
    except FileNotFoundError as e:
        transactions_logger.warning(f"Ошибка: {e}. Путь указан неверно")
        return []
    except json.decoder.JSONDecodeError as s:
        transactions_logger.warning(f"Ошибка: {s}. Файл пуст")
        return []
    return data


path = os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")
# path = r"C:\Users\ADMIN\PycharmProjects\pythonProject3\data\operations.json"
print(get_transactions(path))
