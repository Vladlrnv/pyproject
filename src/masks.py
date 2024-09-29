import logging

start_logger = logging.getLogger("get_mask")
file_handler = logging.FileHandler(r"C:\Users\ADMIN\PycharmProjects\pythonProject3\logs\logs.log", "w")
file_formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
file_handler.setFormatter(file_formatter)
start_logger.addHandler(file_handler)
start_logger.setLevel(logging.INFO)


def get_mask_card_number(card_number: str) -> str:
    """Функция маскирует часть номера карты"""
    start_logger.info(f"Начало работы программы. Получен номер счета: {card_number}")
    if len(card_number) == 16 and card_number.isdigit():
        start_logger.info(f"Номер карты скрыт: {card_number[:4]} {card_number[4:6]}{"**"} {"****"} " f"{card_number[12:]}")
        return f"{card_number[:4]} {card_number[4:6]}{"**"} {"****"} " f"{card_number[12:]}"
    else:
        start_logger.info(f"Введен неверный номер карты")
        return str(None)


get_mask_card_number(input())


def get_mask_account(account_number: str) -> str:
    """Функция маскирует часть номера счета"""
    start_logger.info(f"Начало работы программы. Получен номер карты: {account_number}")
    if len(account_number) == 20 and account_number.isdigit():
        start_logger.info(f"Номер счета скрыт: {"**"}{account_number[-4:]}")
        return f"{"**"}{account_number[-4:]}"
    else:
        start_logger.info(f"Введен неверный номер счета")
        return str(None)


get_mask_account(input())
