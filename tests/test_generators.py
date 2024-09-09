import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(gen):
    generator = filter_by_currency(gen)
    assert next(generator) == {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
                               'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
                               'description': 'Перевод организации', 'from': 'Счет 75106830613657916952',
                               'to': 'Счет 11776614605963066702'}


def test_filter_by_currency_empty():
    with pytest.raises(SystemExit, match="Нет транзакций") as exit_:
        generator = filter_by_currency([])
        assert next(generator) == exit_


def test_filter_by_currency_no_cur(gen):
    with pytest.raises(SystemExit, match="В транзакциях нет такой валюты") as ex:
        generator = filter_by_currency(gen, 'EU')
        assert next(generator) == ex


def test_transaction_descriptions_empty():
    with pytest.raises(SystemExit, match="Нет транзакций") as exit_:
        generator = transaction_descriptions([])
        assert next(generator) == exit_


@pytest.mark.parametrize("index, expected", [
    ([0], "Перевод организации"),
    ([1], "Перевод со счета на счет")
])
def test_transaction_descriptions(index, expected, gen):
    generator = transaction_descriptions(gen)
    assert next(generator)


@pytest.mark.parametrize("start, stop, expected", [
    (0, 1, '0000 0000 0000 0000'),
    (9999999999999999, 9999999999999999, '9999 9999 9999 9999')
])
def test_card_number_generator(start, stop, expected):
    generator = card_number_generator(start, stop)
    assert next(generator) == expected
