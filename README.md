# Operations Project

Этот проект позволяет выводить последние 5 выполненных операций из файла `operations.json`.

## Установка

1. Клонируйте репозиторий:
    ```bash
    git clone <url>
    cd operations_project
    ```

2. Создайте и активируйте виртуальное окружение:
    ```bash
    python -m venv venv
    source venv/bin/activate  
    ```

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

## Использование

Запустите функцию `reading_filter_sorting` с указанием файла `operations.json`:
```python
from operations.operations import reading_filter_sorting

reading_filter_sorting('operations.json')