# import json
#
# with open('operations.json', "r", encoding="utf-8") as f:
#     file_content = f.read()
#     templates = json.loads(file_content)
#     # print(templates)
# def filter_sort(templates):
#     items_list = [item for item in templates if item.get("state") == "EXECUTED"]
#     items_list.sort(key=lambda x: x.get("date"), reverse=True)  # todo почитать про key=lamda
#     items_list_last = items_list[0:5]
#     return items_list_last
#     # print(items_list_last)
#
#
# def prepare_message(items_list_last):
#     result = []
#     for item in items_list_last:
#         description = item.get("description")
#         date = item.get('date')
#         from_x = item.get('from', '')  # Значение по умолчанию, если 'from' не существует или равен None
#         to = item.get('to', '')  # Значение по умолчанию, если 'to' не существует или равен None
#         last_four_digits = from_x[-4:]  # Получаем последние четыре цифры номера карты/счета
#         to_account_last_four_digits = to[-4:]  # Получаем последние четыре цифры номера счета
#         operationAmount = item.get('operationAmount').get('amount')
#         operationAmount_1 = item.get('operationAmount').get('currency').get('name')
#         result.append(f"{date} {description}\n{from_x} -> Счет {to_account_last_four_digits}\n{operationAmount} {operationAmount_1}")
#     return result
#
# # Пример использования:
# x = filter_sort(templates)
# output = prepare_message(x)
# for line in output:
#     print(line)
import json
from datetime import datetime

with open('operations.json', "r", encoding="utf-8") as f:
    file_content = f.read()
    templates = json.loads(file_content)

def filter_and_sort(templates):
    items_list = [item for item in templates if item.get("state") == "EXECUTED"]
    items_list.sort(key=lambda x: parse_date(x.get("date")), reverse=True)
    last_items = items_list[:5]
    return last_items

def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%d.%m.%Y")
    except ValueError:
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")

def prepare_message(last_items):
    result = []
    for item in last_items:
        description = item.get("description")
        date = item.get('date')
        from_x = item.get('from', '')
        to = item.get('to', '')
        last_four_digits_from = from_x[-4:] if from_x else ''
        last_four_digits_to = to[-4:] if to else ''
        operation_amount = item.get('operationAmount').get('amount')
        operation_currency = item.get('operationAmount').get('currency').get('name')
        formatted_date = parse_date(date).strftime("%d.%m.%Y")
        sender_info = f"Visa Platinum 7000 {from_x[-9:-5]}** **** {last_four_digits_from}" if from_x else "N/A"
        receiver_info = f" -> Счет **{last_four_digits_to}" if to else " -> N/A"
        result.append(f"{formatted_date} {description}\n{sender_info}{receiver_info}\n{operation_amount} {operation_currency}")
    return result

# Пример использования:
x = filter_and_sort(templates)
output = prepare_message(x)
for line in output:
    print(line)




