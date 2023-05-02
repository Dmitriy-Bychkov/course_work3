import pytest

from utils import func
from utils.func import load_bank_data, converting_with_missing_keys, sorting_by_date_for_5_operations


def test_load_bank_data():
    assert func.load_bank_data('../operations.json') == load_bank_data('../operations.json')


@pytest.fixture
def sample_data():
    return [
        {
            "state": "EXECUTED",
            "date": "2021-01-01",
            "description": "Test transaction 1",
            "from": "John",
            "to": "Mary",
            "operationAmount": {
                "amount": 100,
                "currency": {
                    "name": "USD"
                }
            }
        },
        {
            "state": "PENDING",
            "date": "2021-01-02",
            "description": "Test transaction 2",
            "from": "Mary",
            "to": "John",
            "operationAmount": {
                "amount": 200,
                "currency": {
                    "name": "EUR"
                }
            }
        },
        {
            "state": "EXECUTED",
            "date": "2021-01-03",
            "description": "Test transaction 3",
            "to": "Mary",
            "operationAmount": {
                "amount": 300,
                "currency": {
                    "name": "GBP"
                }
            }
        }
    ]

def test_converting_with_missing_keys(sample_data):
    expected_result = [
        {
            "date": "2021-01-01",
            "description": "Test transaction 1",
            "from": "John",
            "to": "Mary",
            "amount": 100,
            "currency": "USD"
        },
        {
            "date": "2021-01-03",
            "description": "Test transaction 3",
            "from": None,
            "to": "Mary",
            "amount": 300,
            "currency": "GBP"
        }
    ]
    assert converting_with_missing_keys(sample_data) == expected_result


@pytest.fixture
def sample_data2():
    return [
        {
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "description": "Test transaction 1",
            "from": "John",
            "to": "Mary",
            "operationAmount": {
                "amount": 100,
                "currency": {
                    "name": "USD"
                }
            }
        },
        {
            "state": "PENDING",
            "date": "2019-07-03T18:35:29.512364",
            "description": "Test transaction 2",
            "from": "Mary",
            "to": "John",
            "operationAmount": {
                "amount": 200,
                "currency": {
                    "name": "EUR"
                }
            }
        },
        {
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "description": "Test transaction 3",
            "to": "Mary",
            "operationAmount": {
                "amount": 300,
                "currency": {
                    "name": "GBP"
                }
            }
        }
    ]

def test_sorting_by_date_for_5_operations(sample_data2):
    expected_result = [
        {
        'date': '2019-08-26T10:50:58.294041',
        'description': 'Test transaction 1',
        'from': 'John',
        'operationAmount': {'amount': 100, 'currency': {'name': 'USD'}},
        'state': 'EXECUTED',
        'to': 'Mary'
        },
        {
        'date': '2019-07-03T18:35:29.512364',
        'description': 'Test transaction 2',
        'from': 'Mary',
        'operationAmount': {'amount': 200, 'currency': {'name': 'EUR'}},
        'state': 'PENDING',
        'to': 'John'
        },
        {
        'date': '2018-06-30T02:08:58.425572',
        'description': 'Test transaction 3',
        'operationAmount': {'amount': 300, 'currency': {'name': 'GBP'}},
        'state': 'EXECUTED',
        'to': 'Mary'
        }
    ]
    assert sorting_by_date_for_5_operations(sample_data2) == expected_result


def test_with_errors():
    with pytest.raises(FileNotFoundError):
        load_bank_data('operations.json')

    with pytest.raises(TypeError):
        sorting_by_date_for_5_operations('26464')


