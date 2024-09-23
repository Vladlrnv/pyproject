import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def converter(transaction: dict) -> Any:
    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return amount
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
            return round(data, 2)


# transaction = {
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
#   }
# converter(transaction)
