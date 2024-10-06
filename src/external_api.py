import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def converter(transaction: Any) -> Any:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    amount = transaction[0]["operationAmount"]["amount"]
    currency = transaction[0]["operationAmount"]["currency"]["code"]
    if currency == "RUB":
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


# transaction = {
#     "id": 895315941,
#     "state": "EXECUTED",
#     "date": "2018-08-19T04:27:37.904916",
#     "operationAmount": {
#       "amount": "56883.54",
#       "currency": {
#         "name": "USD",
#         "code": "USD"
#       }
#     },
#     "description": "Перевод с карты на карту",
#     "from": "Visa Classic 6831982476737658",
#     "to": "Visa Platinum 8990922113665229"
#   }

# print(converter(transaction))
