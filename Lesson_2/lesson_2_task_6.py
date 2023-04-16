'''
6. Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс
   ItemDiscountReport на два класса. Инициализировать классы необязательно.
   Внутри каждого поместить функцию get_info, которая в первом классе будет
   отвечать за вывод названия товара, а вторая — его цены.
   Далее реализовать выполнение каждой из функции тремя способами.
'''


class ItemDiscount:

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, val):
        self.__price = val


class ItemDiscountReport(ItemDiscount):

    def __init__(self, name, price, discount=0):
        super().__init__(name, price)
        self.discount = discount

    def __str__(self):
        discount_price = self.price - self.price * (self.discount / 100)
        return f'Цена товара со скидкой: {discount_price}'

    def get_parent_data(self):
        print(f'name: {self.name}, price: {self.price}')


class ItemDiscountReportName(ItemDiscountReport):

    def get_info(self):
        print(self.name)


class ItemDiscountReportPrice(ItemDiscountReport):

    def get_info(self):
        print(self.price)


if __name__ == '__main__':
    item_discount_1 = ItemDiscountReportName('notebook', 250000)
    item_discount_2 = ItemDiscountReportPrice('notebook', 250000)

    # 1
    item_discount_1.get_info()
    item_discount_2.get_info()

    # 2
    for i in (item_discount_1, item_discount_2):
        i.get_info()

    # 3
    def get_info(*args):
        for arg in args:
            arg.get_info()

    get_info(item_discount_1, item_discount_2)
