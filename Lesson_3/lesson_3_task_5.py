'''
5. Усовершенствовать первую функцию из предыдущего примера. Необходимо во втором списке часть строковых
   значений заменить на значения типа example345 (строка+число). Далее — усовершенствовать вторую функцию
   из предыдущего примера (функцию извлечения данных). Дополнительно реализовать поиск определенных подстрок
   в файле по следующим условиям: вывод первого вхождения, вывод всех вхождений. Реализовать замену всех найденных
   подстрок на новое значение и вывод всех подстрок, состоящих из букв и цифр и имеющих пробелы только в начале
   и конце — например, example345.
'''

from os import path
from random import randint
import re


def print_file(file_name, substr):
    with open(path.abspath(file_name), 'r', encoding='utf-8') as f:
        text = f.read()

        # Первое вхождение
        print(re.search(substr, text).group(0))

        # Все вхождения
        for line in re.findall(substr, text):
            print(line)

        # Заменим текст на другой
        text = re.sub(substr, 'nonexample', text)

        with open(path.abspath(file_name), 'w+', encoding='utf-8') as f:
            f.write(text)

        # Выводим элементы, состоящие из букв и цифр и имеющих пробелы только в начале и конце
        pattern = '\s+\d+[a-zA-Z]+\w*\s+|\s+[a-zA-Z]+\d+\w*\s+'
        for line in re.findall(pattern, text):
            print(line)


def fill_file(file_name, substr):
    if path.exists(path.abspath(file_name)):
        print(f'Файл {file_name} существует. Обработка завершена.')
    else:
        with open(file_name, 'w', encoding='utf-8') as f:
            # Примем, что списки одинаковой длины.
            list_numbers = [randint(1, 100) for i in range(1, 45)]
            list_symbols = [f'{substr}{randint(100, 1000)}' if i % 10 == 0 else chr(randint(97, 120)) for i in
                            range(1, 45)]

            for a, b in zip(list_numbers, list_symbols):
                f.write(f'{a} {b} \n')

        print_file(file_name, substr)


if __name__ == '__main__':
    # Перед запуском удалить файл test_task_5.txt
    fill_file('test_task_5.txt', 'example')
