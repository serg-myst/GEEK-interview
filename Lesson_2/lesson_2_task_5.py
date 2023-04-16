'''
5. Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в качестве
   аргумента в дочерний класс. Выполнить перегрузку методов конструктора дочернего класса
   (метод init, в который должна передаваться переменная — скидка), и перегрузку метода
   str дочернего класса. В этом методе должна пересчитываться цена и возвращаться результат — цена товара со скидкой.
   Чтобы все работало корректно, не забудьте инициализировать дочерний и родительский классы
   (вторая и третья строка после объявления дочернего класса).
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


if __name__ == '__main__':
    item_discount = ItemDiscount('notebook', 250000)

    item_discount.price = 260000  # устанавливаем новую цену

    item_discount_report = ItemDiscountReport(item_discount.name, item_discount.price, 10)
    item_discount_report.get_parent_data()

    print(str(item_discount_report))
