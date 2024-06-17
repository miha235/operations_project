import pytest

from operations.main import date_format, masking_account_det, reading, filter_sorting, print_operations


# Тесты для функции date_format
def test_date_format_valid_input():
    assert date_format("2019-04-11T23:10:21.514616") == "11.04.2019"


def test_date_format_invalid_input():
    with pytest.raises(ValueError):
        date_format("invalid_date_string")


# Тесты для функции masking_account_det
def test_masking_account_det_card_number():
    assert masking_account_det("МИР 8201420097886664") == "МИР 8201 42XX XXXX 6664"


def test_masking_account_det_bank_account():
    assert masking_account_det("Счет 67667879435628279708") == "Счет XX 9708"


def test_masking_account_det_invalid_input():
    assert masking_account_det(None) == " ??? "


# Тесты для функции reading

def test_reading_valid_input():
    mock_data = [
        {
            "id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации", "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"},
        {
            "id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации", "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },
    ]

    expected_data = mock_data
    assert reading('../data/operations.json') == expected_data


# Случай с отсутствием файла
def test_reading_invalid_input():
    with pytest.raises(FileNotFoundError):
        reading('nonexistent_file.json')


# Тесты для функции filter_and_sort

# Заранее подготовленные данные для тестирования

test_data = [
    {
        "id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации", "from": "Maestro 1596837868705199", "to": "Счет 64686473678894779589"},
    {
        "id": 41428829, "state": "EXECUTED", "date": "2019-07-16T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации", "from": "MasterCard 7158300734726758", "to": "Счет 35383033474447895560"},
    {
        "id": 441945886, "state": "CANCEL", "date": "2019-08-06T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации", "from": "Maestro 1596837868705199", "to": "Счет 64686473678894779589"},
    {
        "id": 41428829, "state": "EXECUTED", "date": "2019-08-06T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации", "from": "MasterCard 7158300734726758", "to": "Счет 35383033474447895560"},
    {
        "id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации", "from": "MasterCard 7158300734726758", "to": "Счет 35383033474447895560"},
]

# Ожидаемый результат сортировки
expected_result = [{'amount': '31957.58',
                    'currency': 'руб.',
                    'date': '26.08.2019',
                    'description': 'Перевод организации',
                    'from_account': 'Maestro 1596 83XX XXXX 5199',
                    'to_account': 'Счет XX 9589'},
                   {'amount': '8221.37',
                    'currency': 'USD',
                    'date': '06.08.2019',
                    'description': 'Перевод организации',
                    'from_account': 'MasterCard 7158 30XX XXXX 6758',
                    'to_account': 'Счет XX 5560'},
                   {'amount': '8221.37',
                    'currency': 'USD',
                    'date': '16.07.2019',
                    'description': 'Перевод организации',
                    'from_account': 'MasterCard 7158 30XX XXXX 6758',
                    'to_account': 'Счет XX 5560'},
                   {'amount': '8221.37',
                    'currency': 'USD',
                    'date': '03.07.2019',
                    'description': 'Перевод организации',
                    'from_account': 'MasterCard 7158 30XX XXXX 6758',
                    'to_account': 'Счет XX 5560'}]

def test_filter_and_sort_operations():
    sorted_operations = filter_sorting(test_data)
    assert sorted_operations == expected_result, "The operations were not sorted correctly"

@pytest.fixture
def mock_data():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }
    ]

def test_print_operations(capfd, mock_data):

    formatted_operations = filter_sorting(mock_data)
    print_operations(formatted_operations)

# capfd.readouterr() захватывает весь вывод, отправленный в stdout и stderr во время выполнения теста.
    # Возвращаются два значения: out для стандартного вывода и err для вывода ошибок.

    out, err = capfd.readouterr()
    expected_output = (
        "26.08.2019 Перевод организации\n"
        "Maestro 1596 83XX XXXX 5199 -> Счет XX 9589\n"
        "31957.58 руб.\n\n"
        "03.07.2019 Перевод организации\n"
        "MasterCard 7158 30XX XXXX 6758 -> Счет XX 5560\n"
        "8221.37 USD\n\n"
        "30.06.2018 Перевод организации\n"
        "Счет XX 6952 -> Счет XX 6702\n"
        "9824.07 USD\n\n"
    )
    assert out == expected_output
    assert err == ""
