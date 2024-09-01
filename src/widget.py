from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_input: str) -> str:
    """Функция возвращает строку с замаскированным номером"""
    if "Счет" in user_input:
        name = user_input.split()[0]
        card_number = user_input.split()[1]
        return f"{name} {get_mask_account(card_number)}"

    elif "Visa" in user_input:
        name = " ".join(user_input.split()[0:2])
        card_number = user_input.split()[2]
        return f"{name} {get_mask_card_number(card_number)}"
    else:
        name = user_input.split()[0]
        card_number = user_input.split()[1]
        return f"{name} {get_mask_card_number(card_number)}"


print(mask_account_card("Счет 73654108430135871234"))


def get_date(date: str) -> str:
    """Функция возвращает дату в формате ДД.ММ.ГГГГ"""
    d = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    return d.strftime("%d.%m.%Y")
    # my_date = date.split("T")
    # new_date = my_date[0]
    # is_date = new_date.split("-")
    # is_date.reverse()
    # correct_date = ".".join(is_date)
    # return correct_date


print(get_date("2023-12-22T02:26:18.671407"))
