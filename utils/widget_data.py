class BankData:
    def __init__(self, date_time, to_account_number, from_account_number=None):
        self.date_time = date_time
        self.to_account_number = to_account_number
        if from_account_number is None:
            from_account_number = 'XXXX XXXX XXXX XXXX'
        self.from_account_number = from_account_number


    def get_right_data(self):
        '''
        Возвращает дату в нужном нам виде ДД.ММ.ГГГГ.
        '''

        initial_data = self.date_time.split('T')[0]
        not_converted_data = initial_data.split('-')
        converted_data = '.'.join(not_converted_data[::-1])

        return converted_data


    def mask_end_account_number(self):
        '''
        Преобразует и выводит строку с назначением платежа 'Куда'
        в формат вывода счета по маске - **XXXX.
        '''

        splitted_str = self.to_account_number.split(' ')[-1]
        numbers_mask = '*' * 2 + splitted_str[-4:]

        return ' '.join(self.to_account_number.split(' ')[:-1]) + ' ' + numbers_mask


    def mask_full_account_number(self):
        '''
        Преобразует и выводит строку с назначением платежа 'Откуда'
        в формат вывода счета по маске - XXXX XX** **** XXXX.
        '''

        splitted_str = self.from_account_number.split(' ')[-1]
        numbers_mask = '*' * (len(splitted_str) - 10)
        str_with_mask = splitted_str[:6] + numbers_mask + splitted_str[-4:]
        finished_str = ' '.join([str_with_mask[i:i + 4] for i in range(0, len(str_with_mask), 4)])

        return ' '.join(self.from_account_number.split(' ')[:-1]) + ' ' + finished_str


    def __repr__(self):
        return f'{self.__class__.__name__} ' \
               f'{self.date_time}, ' \
               f'{self.payment_purpose}, ' \
               f'{self.to_account_number}, ' \
               f'{self.from_account_number}'