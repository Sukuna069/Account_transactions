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

def filter_sort(templates):
    # Фильтруем элементы с состоянием "EXECUTED" и сортируем по дате (от новых к старым)
    items_list = [item for item in templates if item.get("state") == "EXECUTED"]
    items_list.sort(key=lambda x: get_date(x.get("date")), reverse=True)
    # Берем первые пять элементов из отфильтрованного и отсортированного списка
    items_list_last = items_list[:5]
    return items_list_last

def get_date(date_string):
    # Функция для преобразования даты из строки в объект datetime
    try:
        return datetime.strptime(date_string, "%d.%m.%Y")
    except ValueError:
        # Если дата не соответствует ожидаемому формату, пробуем преобразовать из формата ISO 8601
        return datetime.fromisoformat(date_string).date()

def mask_card_number(card_number):
    # Функция для замаскирования номера карты
    visible_digits = 6
    masked_portion = "*" * 2  # Количество маскированных символов между блоками видимых цифр
    return f"{card_number[:visible_digits]} {masked_portion} **** {card_number[-4:]}"

def prepare_message(items_list_last):
    result = []
    for item in items_list_last:
        description = item.get("description")
        date = get_date(item.get('date')).strftime("%d.%m.%Y")
        from_x = mask_card_number(item.get('from', ''))  # Замаскированный номер карты отправителя
        to = mask_card_number(item.get('to', ''))  # Замаскированный номер карты получателя
        operationAmount = item.get('operationAmount').get('amount')
        operationAmount_1 = item.get('operationAmount').get('currency').get('name')
        result.append(f"{date} {description}\n{from_x} -> Счет {to}\n{operationAmount} {operationAmount_1}")
    return result

# Пример использования:
x = filter_sort(templates)
output = prepare_message(x)
for line in output:
    print(line)


