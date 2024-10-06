# -*- coding: utf-8 -*-
import os
from typing import Any

from src.generators import filter_by_currency
from src.pd_trans import get_transactions_csv, get_transactions_excel
from src.processing import filter_by_state, sort_by_date
from src.selection import search
from src.utils import get_transactions
from src.widget import get_date, mask_account_card

path_json = os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")
path_csv = os.path.join(os.path.dirname(__file__), "..", "data", "transactions.csv")
path_excel = os.path.join(os.path.dirname(__file__), "..", "data", "transactions_excel.xlsx")


def main() -> Any:
    """Функцияб которая отвечает за основную логику проекта и связывает функциональности между собой"""
    while True:
        menu = input(
            """Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
"""
        )
        if menu == "1":
            print("Для обработки выбран JSON-файл.")
            transaction = get_transactions(path_json)
            break
        elif menu == "2":
            print("Для обработки выбран CSV-файл.")
            transaction = get_transactions_csv(path_csv)
            break
        elif menu == "3":
            print("Для обработки выбран EXCEL-файл.")
            transaction = get_transactions_excel(path_excel)
            break
        else:
            print("Пожалуйста, выберите один из предложенных вариантов.")

    while True:
        states = ["EXECUTED", "CANCELED", "PENDING"]
        state = input(
            """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
"""
        ).upper()
        if state not in states:
            print(f"Статус операции {state} недоступен.")
        else:
            break
    print(f"Операции отфильтрованы по статусу {state}")
    you_operations = filter_by_state(transaction, state)

    date_sort = input("Отсортировать операции по дате? Да/Нет ").lower()
    if date_sort == "да":
        if input("Отсортировать по возрастанию или по убыванию? ").lower() == "по возрастанию":
            revers = False
        else:
            revers = True
        you_operations = sort_by_date(you_operations, revers)

    filter_by_rub = input("Выводить только рублевые транзакции? Да/Нет ").lower()
    if filter_by_rub == "да":
        transactions_by_rub = filter_by_currency(you_operations, "RUB")
        filtered_transactions = list(transactions_by_rub)
    else:
        transactions_by_rub = filter_by_currency(you_operations)
        filtered_transactions = list(transactions_by_rub)

    filter_by_word = input("Отфильтровать список транзакций по определенному слову в описании? Да / Нет ").lower()
    if filter_by_word == "да":
        word = input("Введите описание транзацкии. Например: 'Открытие вклада' ").capitalize()
        result_transactions = search(filtered_transactions, word)
    else:
        result_transactions = filtered_transactions

    if len(result_transactions) == 0:
        return "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
    else:
        print(
            f"""Распечатываю итоговый список транзакций...
        Всего банковских операций в выборке: {len(result_transactions)}"""
        )
    for result in result_transactions:
        date = get_date(result["date"])
        currency = result["operationAmount"]["currency"]["name"]
        if result["description"] == "Открытие вклада":
            from_to = mask_account_card(result["to"])
        else:
            from_to = mask_account_card(result["from"]) + " -> " + mask_account_card(result["to"])
        amount = result["operationAmount"]["amount"]
        print(
            f"""{date} {result["description"]}
{from_to}
Сумма: {amount} {currency}"""
        )


print(main())
