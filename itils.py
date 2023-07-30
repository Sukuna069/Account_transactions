# from main import templates
# def filter_sort(templates):
#     items_list = [item for item in templates if item.get("state") == "EXECUTED"]
#     items_list.sort(key=lambda x: x.get("date"), reverse=True)  # todo почитать про key=lamda
#     items_list_last = items_list[0:5]
#     return items_list_last
#     # print(items_list_last)
#
# def prepare_message(items_list_last):
#     result = []
#     for item in items_list_last:
#         description = item.get("description")
#         date = item.get('date')
#         from_x = item.get('from')
#         to = item.get('to')
#         operationAmount = item.get('operationAmount').get('amount')
#         operationAmount_1 = item.get('operationAmount').get('currency').get('name')
#         result.append(f"({date} {description}{from_x}\n{to}\n{operationAmount} {operationAmount_1}")
#     print(result)
# x = filter_sort(templates)
# prepare_message(x)
