'''
Вывести таблицу умножения:

1 X 1 = 1
1 X 2 = 2
...
1 X 10 = 10
-----
2 X 1 = 2
2 X 2 = 4
...
N X 10 = 10N

Параметр N задается с клавиатуры (или в виде аргумента скрипта, по желанию)
Между разделами вывести разделитель в виде 5 дефисов
'''

factor = int(input(f'Введите целое число: '))
delimiter = '-----'

for i in range(1, factor+1):
    for j in range(1, 11):
        print(f'{i} X {j} = {i*j}')
    print(delimiter)