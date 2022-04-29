# Домашнее задание к лекции 5.«Decorators»
# 3. Применить написанный логгер к приложению из предыдущего д/з.
# Предыдущее домашнее задание к лекции «Iterators. Generators. Yield»
# 1. Написать итератор, который принимает список списков, и возвращает их плоское представление,
# т.е последовательность состоящую из вложенных элементов.
# Должен отпечататься каждый элемент каждого вложенного списка
# а комперхеншн, выражение вернет плоский список flat_list = [item for item in FlatIterator(nested_list)]
# во flat_list должен быть такой список: ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
# 2. Написать генератор, который принимает список списков, и возвращает их плоское представление.
# Должен отпечататься каждый элемент каждого вложенного списка
# 3.* Написать итератор аналогичный итератору из задания 1, но обрабатывающий списки с любым уровнем вложенности
# 4.* Написать генератор аналогичный генератор из задания 2, но обрабатывающий списки с любым уровнем вложенности
import os
from logger import logger, path_logger

print(f'Введите каталог для записи логов:\nРабочий каталог: {os.getcwd()}')
catalogue = input()
if not os.path.isdir(catalogue) and catalogue != '':
    os.mkdir(catalogue)
path_file = os.path.join(os.getcwd(), catalogue)


# 1. Итератор:
@logger
class FlatIterator:
    def __init__(self, list_of_lists):
        self.flat = []
        for item in list_of_lists:
            self.flat += item

    def __iter__(self):
        return self

    def __next__(self):
        if not self.flat:
            raise StopIteration
        item = self.flat[0]
        del self.flat[0]
        return item


# 2. Генератор.
@logger
def flat_generator(list_of_lists):
    for some_list in list_of_lists:
        for item in some_list:
            yield item


# 3*. Итератор
@path_logger(path_file)
class FlatDeepIterator:
    def __init__(self, deep_of_lists):
        self.flat = []
        for item in deep_of_lists:
            if isinstance(item, list):
                self.flat.extend(FlatDeepIterator(item))
            else:
                self.flat.append(item)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.flat:
            raise StopIteration
        item = self.flat[0]
        del self.flat[0]
        return item


# 4*. Генератор.
@path_logger(path_file)
def flat_deep_generator(deep_of_lists):
    for item in deep_of_lists:
        if isinstance(item, list):
            yield from flat_deep_generator(item)
        else:
            yield item


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

deep_list = [
    ['a', 'b', 'c',
     ['d', 'e', 'f', 'h', False,
      [1, 2, None]]],
]

if __name__ == '__main__':
    print('1. Итератор:')

    print(f'nested_list:{nested_list}')
    for item_ in FlatIterator(nested_list):
        print(item_)

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)

    print('\n2. Генератор:')

    print(f'nested_list:{nested_list}')
    for item in flat_generator(nested_list):
        print(item)
    print(list(flat_generator(nested_list)))

    print('\n3*. Итератор:')

    print(f'\nnested_list:{nested_list}')
    for item_ in FlatDeepIterator(nested_list):
        print(item_)
    flat_list = [item for item in FlatDeepIterator(nested_list)]
    print(flat_list)

    print(f'\ndeep_list: {deep_list}')
    for item_ in FlatDeepIterator(deep_list):
        print(item_)
    flat_list = [item for item in FlatDeepIterator(deep_list)]
    print(flat_list)

    print('\n4*. Генератор:')

    print(f'\nnested_list:{nested_list}')
    for item in flat_deep_generator(nested_list):
        print(item)
    print(list(flat_deep_generator(nested_list)))

    print(f'\ndeep_list: {deep_list}')
    for item in flat_deep_generator(deep_list):
        print(item)
    print(list(flat_deep_generator(deep_list)))
