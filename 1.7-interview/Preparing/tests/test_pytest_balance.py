import pytest
from balance import balance


fixtures = [
        ('(((([{}]))))', 'Сбалансированно'),
        ('[([])((([[[]]])))]{()}', 'Сбалансированно'),
        ('{{[()]}}', 'Сбалансированно'),
        ('}{}', 'Несбалансированно'),
        ('{{[(])]}}', 'Несбалансированно'),
        ('[[{())}]', 'Несбалансированно')
]


@pytest.mark.parametrize('input_string, answer', fixtures)
def test_balance(input_string: str, answer: str):
    assert balance(input_string) == answer
