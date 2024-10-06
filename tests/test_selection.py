# -*- coding: utf-8 -*-
from typing import Any

from src.selection import search, search_by_categories


def test_search(searching: list[dict]) -> None:
    result = search(searching, "Открытие вклада")
    assert result == [
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431",
        }
    ]


def test_search_wrong(searching: list[dict]) -> None:
    result = search(searching, "some_text")
    assert result == []


def test_search_by_categories(searching: list[dict], categories: list) -> None:
    result = search_by_categories(searching, categories)
    assert result == {"Открытие вклада": 1, "Перевод со счета на счет": 2}


def test_search_by_categories_wrong(searching: list[dict]) -> None:
    result = search_by_categories(searching, [])
    assert result == {}
