# Домашнее задание к лекции 5.«Decorators»
# 1. Написать декоратор - логгер. Он записывает в файл дату и время вызова функции,
#    имя функции, аргументы, с которыми вызвалась и возвращаемое значение.
# 2. Написать декоратор из п.1, но с параметром – путь к логам.
import os
from logger import logger, path_logger
print(f'Введите каталог для записи логов:\nРабочий каталог: {os.getcwd()}')
catalogue = input()
if not os.path.isdir(catalogue) and catalogue != '':
    os.mkdir(catalogue)
path_file = os.path.join(os.getcwd(), catalogue)


@logger
def addition(a, b):
    return a + b


@path_logger(path_file)
def multiplication(a, b):
    return a * b


if __name__ == "__main__":
    # 1. Декоратор - логгер. Запись в файл logger.txt в текущий каталог
    for i in range(100):
        addition(i, i)

    # 2. Параметризированный декоратор с параметром – путь к логам.
    for i in range(100):
        multiplication(i, i)
