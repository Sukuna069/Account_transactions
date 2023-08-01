import pytest
import json
from main import mask_card_number, mask_account_number, format_operation, get_last_executed_operations

# Тестирование функции mask_card_number
def test_mask_card_number():
    assert mask_card_number("1234567812345678") == "1234 **** **** 5678"
    assert mask_card_number("1234-5678-1234-5678") == "1234 **** **** 5678"

# Тестирование функции mask_account_number
def test_mask_account_number():
    assert mask_account_number("123456") == "**3456"

# Тестирование функции format_operation
def test_format_operation():
    operation_data = {
        "date": "2023-07-31T15:30:00.000",
        "description": "Payment",
        "from": "1234567812345678",
        "to": "7890123456789012",
        "operationAmount": {
            "amount": "1000",
            "currency": {
                "name": "USD"
            }
        },
        "state": "EXECUTED"
    }
    expected_output = "31.07.23 Payment\n1234 **** **** 5678 -> **9012\n1000 USD\n"
    assert format_operation(operation_data) == expected_output


# Тестирование функции get_last_executed_operations
def test_get_last_executed_operations():
    # Подготовим тестовые данные
    operations_data = [
        {
            "date": "2023-07-30T12:00:00.000",
            "description": "Payment 1",
            "state": "EXECUTED"
        },
        {
            "date": "2023-07-31T15:30:00.000",
            "description": "Payment 2",
            "state": "EXECUTED"
        },
        {
            "date": "2023-07-29T18:00:00.000",
            "description": "Payment 3",
            "state": "PENDING"
        },
    ]
    # Ожидаемые последние 5 выполненных операций
    expected_operations = [
        {
            "date": "2023-07-31T15:30:00.000",
            "description": "Payment 2",
            "state": "EXECUTED"
        },
        {
            "date": "2023-07-30T12:00:00.000",
            "description": "Payment 1",
            "state": "EXECUTED"
        }
    ]
    assert get_last_executed_operations(operations_data) == expected_operations


