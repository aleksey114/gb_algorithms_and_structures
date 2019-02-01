# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

import random
import sys


def get_size(obj, seen=None):
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0

    seen.add(obj_id)
    if isinstance(obj, dict):
        size += sum([get_size(v, seen) for v in obj.values()])
        size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_size(i, seen) for i in obj])
    return size


def lesson_3_task_07():
    # В одномерном массиве целых чисел определить два наименьших элемента.
    # Они могут быть как равны между собой (оба являться минимальными), так и различаться.
    SIZE = 10
    MIN_ITEM = -5
    MAX_ITEM = 5
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    print(array)

    min_1, min_2 = array[0], array[1]

    for i in range(2, len(array)):
        if array[i] < min_1 or array[i] < min_2:
            if min_1 < min_2:
                min_2 = array[i]
            else:
                min_1 = array[i]

    print(f'Первое число: {min_1}, второе: {min_2}')
    return locals()


def lesson_3_task_05():
    # В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
    SIZE = 20
    MIN_ITEM = -50
    MAX_ITEM = 50
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    print(array)

    number = 0
    pos_number = None

    for pos, item in enumerate(array):
        if item < 0 and abs(item) > abs(number):
            number = item
            pos_number = pos

    if pos_number is not None:
        print(f'Максимальный отрицательный элемент: {number}')
    else:
        print('Отрицательных элементов нет.')
    return locals()


def lesson_3_task_03():
    # В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
    SIZE = 10
    MIN_ITEM = -100
    MAX_ITEM = 100
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    print(array)

    min_pos, max_pos = 0, 0

    for pos in range(1, len(array)):
        if array[min_pos] > array[pos]:
            min_pos = pos
        if array[max_pos] < array[pos]:
            max_pos = pos

    array[min_pos], array[max_pos] = array[max_pos], array[min_pos]
    return locals()


if __name__ == '__main__':
    # Python 3.7.2 - х64 ОС
    print(f'== Для задачи было выделено {get_size(lesson_3_task_03())} байт')
    # Для задачи было выделено 1337 байт
    print(f'== Для задачи было выделено {get_size(lesson_3_task_05())} байт')
    # Для задачи было выделено 1688 байт
    print(f'== Для задачи было выделено {get_size(lesson_3_task_07())} байт')
    # Для задачи было выделено 1187 байт
