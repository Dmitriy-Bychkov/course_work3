import json
from datetime import datetime


def load_bank_data(filename):
    '''
    Загружает данные из файла json и записывает содержимое в переменную.
    '''
    with open(filename, 'r', encoding='utf-8') as file:
        all_data = json.load(file)

    return all_data


def converting_with_missing_keys(global_list):
    '''
    Переконвертирует исходный список словарей, полученный из json, в список словарей
    только с нужными для нашей работы данными.
    Выбирает только те словари, которые сожержат статус операции - EXECUTED.
    А также все пропущенные ключи подставляются и земеняются начением - None.
    '''

    new_dict = []
    for item in global_list:
        new_list = {}
        if item.get('state') == 'EXECUTED':
            new_list['date'] = item['date']
            new_list['description'] = item['description']
            new_list['from'] = item.get('from')
            new_list['to'] = item['to']
            new_list['amount'] = item["operationAmount"]["amount"]
            new_list["currency"] = item["operationAmount"]["currency"]["name"]
            new_dict.append(new_list)

    return new_dict


def sorting_by_date_for_5_operations(converted_list):
    '''
    Сортирует переконвертированный список словарей по дате
    и выбирает последние 5 свежих операций с конца списка.
    '''

    sorted_list_of_dicts = sorted(converted_list, key=lambda k: datetime.strptime(k['date'], '%Y-%m-%dT%H:%M:%S.%f'))
    list_with_5_operations = sorted_list_of_dicts[-5:]
    inverted_list_by_date = list_with_5_operations[::-1]

    return inverted_list_by_date