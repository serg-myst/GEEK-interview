'''
2. Инкапсулировать оба параметра (название и цену) товара родительского класса.
   Убедиться, что при сохранении текущей логики работы программы будет сгенерирована ошибка выполнения.
'''

class ItemDiscount:

    def __init__(self, name, price):
        self.__name = name
        self.__price = price


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        print(f'name: {self.name}, price: {self.price}')


if __name__ == '__main__':
    item_discount = ItemDiscount('notebook', 250000)
    print(item_discount.name, item_discount.price)
    ItemDiscountReport(item_discount.name, item_discount.price).get_parent_data()
