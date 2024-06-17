import json

from datetime import datetime


def date_format(date_string):
    """Форматирование даты перевода"""
    new_date_string = datetime.fromisoformat(date_string).strftime("%d.%m.%Y")
    return new_date_string


def masking_account_det(account_details):
    """Маскировка карты и счета"""
    if account_details:
        if " " in account_details:
            numbers = account_details.split()  # создаем список

        if len(numbers) > 2:
            return f"{numbers[0]} {numbers[1]} {numbers[2][:4]} {numbers[2][4:6]}XX XXXX {numbers[2][-4:]}"

        elif numbers[0] == "Счет":
            return f"{numbers[0]} XX {numbers[1][-4:]}"
        else:
            return f"{numbers[0]} {numbers[1][:4]} {numbers[1][4:6]}XX XXXX {numbers[1][-4:]}"

    return " ??? "


def reading(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        file_data = json.load(file)
        return file_data


def filter_sorting(file_data):
    executed_operations = []
    for data in file_data:
        if data.get('state') == 'EXECUTED':
            executed_operations.append(data)

    executed_operations.sort(key=lambda x: x['date'], reverse=True)

    last_operations = executed_operations[:5]
    formatted_operations = []

    for operation in last_operations:
        date = date_format(operation['date'])
        description = operation['description']
        from_account = masking_account_det(operation.get('from'))
        to_account = masking_account_det(operation.get('to'))
        amount = operation['operationAmount']['amount']
        currency = operation['operationAmount']['currency']['name']

        formatted_operations.append({
            "date": date,
            "description": description,
            "from_account": from_account,
            "to_account": to_account,
            "amount": amount,
            "currency": currency
        })

    return formatted_operations

def print_operations(operations):
    for operation in operations:
        print(f"{operation['date']} {operation['description']}")
        print(f"{operation['from_account']} -> {operation['to_account']}")
        print(f"{operation['amount']} {operation['currency']}\n")


file_data = reading('../data/operations.json')

formatted_operations = filter_sorting(file_data)
print_operations(formatted_operations)