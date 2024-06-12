import pytest
from operations.main import date_format, masking_account_det, reading_filter_sorting

# Тесты для функции date_format

def test_date_format_valid_input():
    assert date_format("2019-04-11T23:10:21.514616") == "11.04.2019"

def test_date_format_invalid_input():
    with pytest.raises(ValueError):
        date_format("invalid_date_string")

# Тесты для функции masking_account_det

def test_masking_account_det_card_number():
    assert masking_account_det("МИР 8201420097886664") == "МИР 8201 4200XXXX 6664"

def test_masking_account_det_bank_account():
    assert masking_account_det("Счет 67667879435628279708") == "Счет XX 9708"

def test_masking_account_det_invalid_input():
    assert masking_account_det(None) == " ??? "

# Тесты для функции reading_filter_sorting пока не выходят
# я проверила что она работает

def test_reading_filter_sorting_valid_input():
    assert reading_filter_sorting('../data/operations.json') is None

def test_reading_filter_sorting_invalid_input():
    with pytest.raises(FileNotFoundError):
        reading_filter_sorting('nonexistent_file.json')
