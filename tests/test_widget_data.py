import pytest

from utils.widget_data import BankData

bank_data = BankData('2019-08-26T10:50:58.294041', 'Счет 64686473678894779589', 'Maestro 1596837868705199')
def test_get_right_data():
    assert bank_data.get_right_data() == '26.08.2019'


def test_mask_end_account_number():
    assert bank_data.mask_end_account_number() == 'Счет **9589'


def test_mask_full_account_number():
    assert bank_data.mask_full_account_number() == 'Maestro 1596 83** **** 5199'


def test_with_errors():
    assert bank_data.get_right_data() != '222'
    with pytest.raises(TypeError):
        bank_data.get_right_data('test') == '352'