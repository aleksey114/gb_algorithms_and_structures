# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

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
print(array)
