'''
4. Написать программу, в которой реализовать две функции. В первой должен создаваться простой текстовый файл.
   Если файл с таким именем уже существует, выводим соответствующее сообщение.
   Необходимо открыть файл и подготовить два списка: с текстовой и числовой информацией.
   Для создания списков использовать генераторы. Применить к спискам функцию zip().
   Результат выполнения этой функции должен быть обработан и записан в файл таким образом,
   чтобы каждая строка файла содержала текстовое и числовое значение. Вызвать вторую функцию.
   В нее должна передаваться ссылка на созданный файл. Во второй функции необходимо реализовать
   открытие файла и простой построчный вывод содержимого. Вся программа должна запускаться по вызову первой функции.
'''

from os import path
from random import randint


def print_file(file_name):
    with open(path.abspath(file_name), 'r', encoding='utf-8') as f:
        for line in f:
            print(line.strip())


def fill_file(file_name):
    if path.exists(path.abspath(file_name)):
        print(f'Файл {file_name} существует. Обработка завершена.')
    else:
        with open(file_name, 'w', encoding='utf-8') as f:
            # Примем, что списки одинаковой длины.
            # Заполним список числами длиной 15 элементов. В тз про размер списка не сказано ничего
            list_numbers = [randint(1, 100) for i in range(1, 16)]
            # Заполним список буквами длиной 15 элементов. В тз про размер списка не сказано ничего
            list_symbols = [chr(randint(97, 120)) for i in range(1, 16)]

            for a, b in zip(list_numbers, list_symbols):
                f.write(f'{a} {b} \n')

        print_file(file_name)


if __name__ == '__main__':
    fill_file('test_task_4.txt')