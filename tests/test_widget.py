from typing import Any

import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "string, expected",
    [
        ("Счет 73654108430135871234", "Счет **1234"),
        ("Visa classic 7365410843013587", "Visa classic 7365 41** **** 3587"),
        ("73654108430135871234", "None"),
    ],
)
def test_mask_account_card(string: str, expected: str) -> Any:
    assert mask_account_card(string) == expected


@pytest.fixture
def date_fix() -> str:
    return "2023-12-22T02:26:18.671407"


def test_get_date(date_fix: str) -> Any:
    assert get_date(date_fix) == "22.12.2023"


@pytest.mark.parametrize("date, expected", [("2023-12-22T02:26:18.671407", "22.12.2023"), ("", "..")])
def test_get_dates(date: str, expected: str) -> Any:
    assert get_date(date) == expected
