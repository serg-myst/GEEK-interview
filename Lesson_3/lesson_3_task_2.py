'''
2. Написать программу, которая запрашивает у пользователя ввод числа. На введенное число она отвечает сообщением,
   целое оно или дробное. Если дробное — необходимо далее выполнить сравнение чисел до и после запятой.
   Если они совпадают, программа должна возвращать значение True, иначе False.
'''


def get_user_number(value):
    if value == int(value):
        return f'Введено целое число {int(value)}'
    else:
        print(f'Введено дробное число {value}')
        list_number = str(value).split('.')
        return list_number[0] == list_number[1]


if __name__ == '__main__':
    while True:
        try:
            value = float(input('Введите число (целое или дробное). Для выхода из программы введите 0: '))
            if value == 0:
                break
            print(get_user_number(value))
        except ValueError:
            print('Введите число!')
            continue

