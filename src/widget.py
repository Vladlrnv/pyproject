from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(requisites: str) -> str:
    """функция общей маскировки карты и счета."""
    parts = requisites.split()  # делим на части по пробелу
    number = parts[-1]  # забираем последний элемент (там всегда номер карты или счёта)
    if requisites.lower().startswith("счет"):  # если пришёл счёт - отдаём номер в ф-цию маскировки номера счёта
        hidden_number = get_mask_account(number)
    else:  # иначе отдаём номер в функцию маскироки карты и получаем скрытый вариант номера
        hidden_number = get_mask_card_number(number)
    parts[-1] = hidden_number  # подставляем скрытый номер обратно
    return " ".join(parts)  # соединяем список в строку


# print(mask_account_card('American Express 1963030970727681'))


def get_date(input_string: str) -> str:
    """Фнкция преобразования даты"""
    data = input_string.split("Т")[0]
    formatted_date = f"{data[8:10]}.{data[5:7]}.{data[:4]}"
    return formatted_date


# print(get_date("2022-06-20T18:08:20Z"))
