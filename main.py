import os.path

from utils.func import load_bank_data, converting_with_missing_keys, sorting_by_date_for_5_operations
from utils.widget_data import BankData


def main():
    filename = os.path.join('operations.json')

    # Последовательно преобразуем данные в конечный для нашей работы список
    all_bank_data = load_bank_data(filename)
    converted_list = converting_with_missing_keys(all_bank_data)
    finished_list_for_print = sorting_by_date_for_5_operations(converted_list)
    print('Ваши последние 5 операций:')
    print()

    # Создаем список экземпляров класса BankData
    for item in finished_list_for_print:
        date_time = item['date']
        payment_purpose = item['description']
        from_account_number = item['from']
        to_account_number = item['to']
        amount = item['amount']
        currency = item['currency']
        bank_data = BankData(date_time, to_account_number, from_account_number)

        print(bank_data.get_right_data() + ' ' + payment_purpose)
        print(bank_data.mask_full_account_number() + ' ' + '->' + ' ' + bank_data.mask_end_account_number())
        print(amount + ' ' + currency)
        print()


if __name__ == '__main__':
    main()
