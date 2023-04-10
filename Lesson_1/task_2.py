'''
Реализовать функцию print_directory_contents(path). Функция принимает имя директории
и выводит ее содержимое, включая содержимое всех поддиректорий (рекурсивно вызывая саму себя).
Использовать os.walk нельзя, но можно использовать os.path.isdir и os.path.isfile
https://pythonworld.ru/moduli/modul-os.html
https://pythonworld.ru/moduli/modul-os-path.html
'''

import os


def print_directory_contents(path):
    current_dir = os.path.join(path)
    for file in os.listdir(current_dir):
        current_file = os.path.join(current_dir, file)
        if os.path.isdir(current_file):
            print(f'DIR: {file}')
            print_directory_contents(current_file)
        else:
            print(f'file: {file}')


if __name__ == '__main__':
    dir_name = 'd:/Программы/'
    print_directory_contents(dir_name)
