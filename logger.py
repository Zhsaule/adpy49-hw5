# Домашнее задание к лекции 5.«Decorators»
# 1. Написать декоратор - логгер. Он записывает в файл дату и время вызова функции,
#    имя функции, аргументы, с которыми вызвалась и возвращаемое значение.
# 2. Написать декоратор из п.1, но с параметром – путь к логам.
# 3. Применить написанный логгер к приложению из любого предыдущего д/з.
import os
from datetime import datetime


def logger(old_function):
    """ 1. Декоратор - логгер. Запись ведется в файл logger.txt в текущий каталог."""
    file_path = os.path.join(os.getcwd(), 'logger.txt')
    print(f'Start logger: {datetime.now()} {file_path} Func: {old_function.__name__}')

    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        with open(file_path, 'a') as f:
            f.write(f'{datetime.now()} - Call function: {old_function.__name__}, ')
            f.write(f'args={args}, kwargs={kwargs}, ')
            f.write(f'Result: {result}\n')
        return result
    return new_function


def path_logger(_file_path):
    """ 2. Параметризированный декоратор, с параметром – путь к логам."""
    def _logger(old_function):
        file_path = os.path.join(_file_path, 'logger_path.txt')
        print(f'Start logger: {datetime.now()} {file_path} Func: {old_function.__name__}')

        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            with open(file_path, 'a') as f:
                f.write(f'{datetime.now()} - Call function: {old_function.__name__}, ')
                f.write(f'args={args}, kwargs={kwargs}, ')
                f.write(f'Result: {result}\n')
            return result
        return new_function
    return _logger


