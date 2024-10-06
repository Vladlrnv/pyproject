import sys
from typing import Any, Generator

# transactions = [
#   {
#     "id": 441945886,
#     "state": "EXECUTED",
#     "date": "2019-08-26T10:50:58.294041",
#     "operationAmount": {
#       "amount": "31957.58",
#       "currency": {
#         "name": "руб.",
#         "code": "RUB"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "Maestro 1596837868705199",
#     "to": "Счет 64686473678894779589"
#   },
#   {
#     "id": 41428829,
#     "state": "EXECUTED",
#     "date": "2019-07-03T18:35:29.512364",
#     "operationAmount": {
#       "amount": "8221.37",
#       "currency": {
#         "name": "USD",
#         "code": "USD"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "MasterCard 7158300734726758",
#     "to": "Счет 35383033474447895560"
#   },
#   {
#     "id": 939719570,
#     "state": "EXECUTED",
#     "date": "2018-06-30T02:08:58.425572",
#     "operationAmount": {
#       "amount": "9824.07",
#       "currency": {
#         "name": "USD",
#         "code": "USD"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "Счет 75106830613657916952",
#     "to": "Счет 11776614605963066702"
#   }]


def filter_by_currency(transactions: Any, currency: str = "USD") -> Any:
    """Функция поочередно возвращает списки транзакций по выбранной валюте"""
    if transactions == []:
        sys.exit("Нет транзакций")
    for i in transactions:
        if i["operationAmount"]["currency"]["code"] == currency:
            yield i


# usd_transactions = filter_by_currency(transactions, "RUB")
# for _ in range(2):
#     print(next(usd_transactions))


def transaction_descriptions(transactions: Any) -> Generator:
    """Функция поочередно возвращает детали операций"""
    if not transactions:
        sys.exit("Нет транзакций")
    for description_operation in transactions:
        yield description_operation.get("description")


# descriptions = transaction_descriptions(transactions)
# for _ in range(3):
#     print(next(descriptions))


def card_number_generator(start: int, stop: int) -> Generator:
    """Функция генерирует номер карты"""
    for number in range(start, stop + 1):
        card_number = str(number)
        while len(card_number) < 16:
            card_number = "0" + card_number
        formatted_card_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield (formatted_card_number)


# for card_number in card_number_generator(1, 5):
#     print(card_number)
