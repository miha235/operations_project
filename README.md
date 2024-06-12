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
    source venv/bin/activate  # Для Windows: venv\Scripts\activate
    ```

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

## Использование

Запустите функцию `print_last_executed_operations` с указанием файла `operations.json`:
```python
from operations.operations import print_last_executed_operations

print_last_executed_operations('operations.json')
Тестирование
Для запуска тестов используйте команду:

bash
Copy code
pytest
perl
Copy code

### Шаг 8: Загрузка на GitHub

1. Добавьте все файлы в репозиторий и сделайте первый коммит:
    ```bash
    git add .
    git commit -m "Initial commit"
    ```

2. Добавьте удаленный репозиторий и отправьте изменения:
    ```bash
    git remote add origin <url вашего репозитория>
    git push -u origin develop
    git push -u origin main
    ```

Теперь ваш проект готов и соответствует всем критериям.