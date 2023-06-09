'''
3. Создать два списка с различным количеством элементов. В первом должны быть записаны ключи,
   во втором — значения. Необходимо написать функцию, создающую из данных ключей и значений словарь.
   Если ключу не хватает значения, в словаре для него должно сохраняться значение None.
   Значения, которым не хватило ключей, необходимо отбросить.
'''

import itertools


# Можно пойти длинным путем через если, но zip_longest позволяет обходить списки разной длины
# Добавим одну проверку, что ключ не равен None
def get_dict(list_keys, list_values):
    return {a: b for a, b in itertools.zip_longest(list_keys, list_values) if a != None}


if __name__ == '__main__':
    # Пример, когда списки одинаковой длины
    list_keys = [1, 2, 3, 4, 5, 6]
    list_values = [1, 2, 3, 4, 5, 6]
    print(get_dict(list_keys, list_values))

    # Пример, когда ключей больше, чем значений
    list_keys = [1, 2, 3, 4, 5, 6]
    list_values = [1, 2, 3, 4]
    print(get_dict(list_keys, list_values))

    # Пример, когда значений больше, чем ключей
    list_keys = [1, 2, 3, 4, 5, 6]
    list_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(get_dict(list_keys, list_values))
