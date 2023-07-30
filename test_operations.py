import json
import pytest
from main import filter_sort, prepare_message

# Фикстура для предоставления тестовых данных
@pytest.fixture
def templates():
    with open('operations.json', "r", encoding="utf-8") as f:
        file_content = f.read()
        return json.loads(file_content)

def test_filter_sort(templates):
    # Вызываем функцию filter_sort с тестовыми данными
    result = filter_sort(templates)

    # Здесь добавляем утверждения для проверки результата
    # Например, проверка на то, что результат не пустой список
    assert result

def test_prepare_message(templates):
    # Вызываем функцию prepare_message с тестовыми данными
    sorted_templates = filter_sort(templates)
    result = prepare_message(sorted_templates)

    # Здесь добавляем утверждения для проверки результата
    # Например, проверка на то, что результат не пустой список
    assert result
