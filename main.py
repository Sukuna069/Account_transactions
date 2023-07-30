import json
from datetime import datetime


def filter_sort(templates):
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
        result.append(
            f"{formatted_date} {description}\n{sender_info}{receiver_info}\n{operation_amount} {operation_currency}")
    return result


if __name__ == "__main__":
    # Пример использования:
    with open('operations.json', "r", encoding="utf-8") as f:
        file_content = f.read()
        templates = json.loads(file_content)

    x = filter_sort(templates)
    output = prepare_message(x)
    for line in output:
        print(line)



