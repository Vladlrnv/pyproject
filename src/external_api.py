import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def converter(transaction: dict) -> Any:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(amount)
    else:
        payload = {"amount": amount, "from": currency, "to": "RUB", "apikey": API_KEY}
        # headers = {"api_key": API_KEY}

        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        response = requests.get(url, params=payload)
        status_code = response.status_code
        if status_code != 200:
            print(response.reason)
        else:
            result = response.json()
            data = result.get("result")
            return float(round(data, 2))


transaction = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {"amount": "31957.58", "currency": {"name": "USD", "code": "USD"}},
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589",
}
print(type(converter(transaction)))
