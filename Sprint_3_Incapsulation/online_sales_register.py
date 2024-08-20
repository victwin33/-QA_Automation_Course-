class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items

    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError(f'Нельзя добавить товар, если в его названии нет символов или их больше 40')
        if name not in self.__item_price:
            raise ValueError(f'Позиция отсутствует в товарном справочнике')
        self.__name_items.append(name)
        self.__number_items += 1

    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise ValueError(f'Позиция отсутствует в чеке')
        self.__name_items.remove(name)
        self.__number_items -= 1

    def check_amount(self):
        total = []
        for name, price in self.__item_price.items():
            if name in self.__name_items:
                total.append(price)

        if len(self.__name_items) > 10:
            discount = sum(total) / 10
            return sum(total) - discount
        else:
            return sum(total)

    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []

        for name, price in self.__tax_rate.items():
            if name in self.__name_items and price == 20:
                twenty_percent_tax.append(name)

        for name, price in self.__item_price.items():
            if name in twenty_percent_tax:
                total.append(price)

        if len(total) > 10:
            nds = (sum(total) / 20) * 0.1

        else:
            nds = sum(total) * 0.2

        return nds

    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []

        for name, price in self.__tax_rate.items():
            if name in self.__name_items and price == 10:
                ten_percent_tax.append(name)

        for name, price in self.__item_price.items():
            if name in ten_percent_tax:
                total.append(price)

        if len(total) > 10:
            nds = (sum(total) / 10) * 0.1

        else:
            nds = sum(total) * 0.1

        return nds

    def total_tax(self):
        ten_percent_tax = self.ten_percent_tax_calculation()
        twenty_percent_tax = self.twenty_percent_tax_calculation()
        return ten_percent_tax + twenty_percent_tax

    @staticmethod
    def get_telephone_number(telephone_number):
        if not (isinstance(telephone_number, int)):
            raise ValueError(f'Необходимо ввести цифры')
        elif (len(str(telephone_number))) > 10:
            raise ValueError(f'Необходимо ввести 10 цифр после "+7"')
        else:
            return print(f'+7{telephone_number}')



