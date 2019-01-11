# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

ROW = 5
COLUMN = 5
MIN_ITEM = -5
MAX_ITEM = 5
array = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(COLUMN)] for _ in range(ROW)]
for line in array:
    for i in line:
        print(f'{i:>4}', end='')
    print()

array_min_in_columns = array[0]
for i in range(1, len(array_min_in_columns)):
    for pos, item in enumerate(array[i]):
        if item < array_min_in_columns[pos]:
            array_min_in_columns[pos] = item

max_number = array_min_in_columns[0]
for i in range(1, len(array_min_in_columns)):
    if array_min_in_columns[i] > max_number:
        max_number = array_min_in_columns[i]

print(f'ЧИсло: {max_number}')