import json
from datetime import datetime
def mask_card_number(card_number):
    # Маскируем номер карты XXXX XX** **** XXXX
    masked_number = card_number[:4] + ' ' + '*' * 4 + ' ' + '*' * 4 + ' ' + card_number[-4:]
    return masked_number

def mask_account_number(account_number):
    # Маскируем номер счета **XXXX
    masked_number = '*' * 2 + account_number[-4:]
    return masked_number

def format_operation(operation):
    # Преобразование даты из исходного формата в объект datetime
    date = datetime.strptime(operation['date'], "%Y-%m-%dT%H:%M:%S.%f")
    # Форматирование даты в нужный формат "11.11.19"
    formatted_date = date.strftime("%d.%m.%y")

    description = operation['description']
    from_account = operation.get('from', '')
    to_account = operation['to']

    # Обработка значения по ключу 'operationAmount'
    operation_amount = operation.get('operationAmount', {})
    amount = operation_amount.get('amount', '')
    currency = operation_amount.get('currency', '').get('name')

    masked_from_account = mask_card_number(from_account) if from_account else ''
    masked_to_account = mask_account_number(to_account)
    formatted_operation = f"{formatted_date} {description}\n{masked_from_account} -> {masked_to_account}\n{amount} {currency}\n"
    return formatted_operation


def get_last_executed_operations(operations_data):
    executed_operations = [operation for operation in operations_data if 'state' in operation and operation['state'] == 'EXECUTED']
    sorted_operations = sorted(executed_operations, key=lambda x: x['date'], reverse=True)
    last_executed_operations = sorted_operations[:5]
    return last_executed_operations

def main():
    with open('operations.json', 'r', encoding='utf-8') as file:
        operations_data = json.load(file)

    last_executed_operations = get_last_executed_operations(operations_data)

    for operation in last_executed_operations:
        formatted_operation = format_operation(operation)
        print(formatted_operation)

if __name__ == "__main__":
    main()
