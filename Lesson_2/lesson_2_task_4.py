'''
4. Реализовать возможность переустановки значения цены товара. Необходимо, чтобы и родительский,
   и дочерний классы получили новое значение цены. Следует проверить это,
   вызвав соответствующий метод родительского класса и функцию дочернего
   (функция, отвечающая за отображение информации о товаре в одной строке).
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

    def get_parent_data(self):
        print(f'name: {self.name}, price: {self.price}')


if __name__ == '__main__':
    item_discount = ItemDiscount('notebook', 250000)

    item_discount.price = 260000  # устанавливаем новую цену

    ItemDiscountReport(item_discount.name, item_discount.price).get_parent_data()