import json

from datetime import datetime

def date_format(date_string):
    """Форматирование даты перевода"""
    new_date_string = datetime.fromisoformat(date_string).strftime("%d.%m.%Y")
    return new_date_string

# print(date_format("2019-04-11T23:10:21.514616"))
# print(date_format.__doc__)

def masking_account_det(account_details):
    """Маскировка карты и счета"""
    if account_details:
        if " " in account_details:
            numbers = account_details.split() # создаем список
            #print(numbers)
        if len(numbers)>2:
            return f"{numbers[0]} {numbers[1]} {numbers[2][:4]} {numbers[2][4:6]}XX XXXX {numbers[2][-4:]}"

        elif numbers[0] == "Счет":
            return f"{numbers[0]} XX {numbers[1][-4:]}"
        else:
            return f"{numbers[0]} {numbers[1][:4]} {numbers[1][4:6]}XX XXXX {numbers[1][-4:]}"

    return " ??? "

"""print(masking_account_det("МИР 8201420097886664"))
print(masking_account_det("Visa Gold 6527183396477720"))
print(masking_account_det("Visa Classic 6216537926639975"))
print(masking_account_det("Счет 67667879435628279708"))"""

def reading_filter_sorting(filename):

    with open(filename, 'r', encoding='utf-8') as file:
        file_data = json.load(file)

    executed_operations = []
    for data in file_data:
        if data.get('state') == 'EXECUTED':
            executed_operations.append(data)

    executed_operations.sort(key=lambda x: x['date'], reverse=True)

    last_operations = executed_operations[:5]


    for operation in last_operations:
        date = date_format(operation['date'])
        description = operation['description']
        from_account = masking_account_det(operation.get('from'))
        to_account = masking_account_det(operation.get('to'))
        amount = operation['operationAmount']['amount']
        currency = operation['operationAmount']['currency']

        print(f"{date} {description}")
        if from_account:
            print(f"{from_account} -> {to_account}")
        else:
            print(f"{to_account}")
        print(f"{amount} {currency}\n")


reading_filter_sorting('../operations.json')

