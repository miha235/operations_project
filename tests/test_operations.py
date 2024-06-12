import pytest
import json
from operations.main import reading_filter_sorting

@pytest.fixture
def sample_operations_data():
    """Загружаем тестовые данные из operations.json"""
    with open('operations.json', 'r') as file:
        return json.load(file)

def test_reading_filter_sorting(sample_operations_data, num):
    """ Вызываем функцию с тестовыми данными"""
    reading_filter_sorting('operations.json')
    captured = num.readouterr()  # Получаем захваченный вывод

    # Проверяем, что вывод содержит ожидаемые строки
    assert "1000 USD\n" in captured.out
    assert "14.06.2023 Transfer" in captured.out
    assert "Visa Gold 6527 1833 XX XXXX 7720 -> Счет XX 3456" in captured.out


    assert "15.06.2023 Payment" in captured.out
    assert "Visa Classic 6216 5379 XX XXXX 9975" in captured.out
    assert "2000 EUR\n" in captured.out

    # Проверяем, что вывод не содержит отмененной операции
    assert "16.06.2023 Withdrawal" not in captured.out

    # Проверяем, что вывод содержит только 5 операций
    assert captured.out.count('\n') == 15  # 5 операций * 3 строки на каждую операцию
