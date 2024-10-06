# -*- coding: utf-8 -*-
import re
from collections import Counter
from typing import Any

categories = [
    "Перевод организации",
    "Открытие вклада",
    "Перевод со счета на счет",
    "Перевод с карты на карту",
    "Перевод с карты на счет",
]
transactions = [
    {
        "id": 587085106,
        "state": "EXECUTED",
        "date": "2018-03-23T10:45:06.972075",
        "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Открытие вклада",
        "to": "Счет 41421565395219882431",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
]


def search(transactions: Any, search_str: Any) -> Any:
    """Функция возвращает список транзакций по условиям, заданным пользователем"""
    pattern = re.compile(search_str, re.IGNORECASE)
    matchies = [transaction for transaction in transactions if pattern.search(transaction.get("description", ""))]
    return matchies


search_str = "jткрытие вклада"
# print(search(transactions, search_str))


def search_by_categories(transactions: Any, categories: Any) -> Any:
    new_list = []
    for transaction in transactions:
        for category in categories:
            if transaction.get("description") == category:
                new_list.append(category)
    my_dict = Counter(new_list)
    return dict(my_dict)


# print(search_by_categories(transactions, categories))
