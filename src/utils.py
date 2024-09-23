import json
from typing import Any


def get_transactions(file_path: Any) -> Any:
    """Функция возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(file_path, encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        return []
    return data


path = r"C:\Users\ADMIN\PycharmProjects\pythonProject3\data\operations.json"
print(get_transactions(path))
