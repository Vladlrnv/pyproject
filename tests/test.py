import pytest

from src.masks import get_mask_card_number, get_mask_account

def test_get_mask_card_number():
    assert get_mask_card_number("7365410843013587") == "7365 41** **** 3587"
    assert get_mask_card_number(" ") == "None"
    assert get_mask_card_number("ADC") == "None"



def test_get_mask_account():
    assert get_mask_account("73654108430135871234") == "**1234"
    assert get_mask_account(" ") == "None"
    assert get_mask_account("ADC") == "None"
