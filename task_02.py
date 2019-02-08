# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
import random


def merge(a, b):
    a_i, b_i = 0, 0
    result = []
    while True:
        if a[a_i] < b[b_i]:
            result.append(a[a_i])
            a_i += 1
            if a_i == len(a):
                result.extend(b[b_i:])
        else:
            result.append(b[b_i])
            b_i += 1
            if b_i == len(b):
                result.extend(a[a_i:])

        if len(result) == len(a) + len(b):
            return result


def merge_sort(array):
    if len(array) >= 2:
        middle = len(array) // 2
        array = merge(merge_sort(array[:middle]), merge_sort(array[middle:]))
    return array


if __name__ == '__main__':
    SIZE = 10
    array = [random.random() * 50 for _ in range(SIZE)]
    print(array)
    result = merge_sort(array)
    print(result)
