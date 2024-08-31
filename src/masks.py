def get_mask_card_number(card_number: str) -> str:
    """Функция маскирует часть номера карты"""
    if len(card_number) == 16 and card_number.isdigit():
        return f"{card_number[:4]} {card_number[4:6]}{"**"} {"****"} " f"{card_number[12:]}"
    else:
        return str(None)


def get_mask_account(account_number: str) -> str:
    """Функция маскирует часть номера счета"""
    if len(account_number) == 20 and account_number.isdigit():
        return f"{"**"}{account_number[-4:]}"
    else:
        return str(None)
