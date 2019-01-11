# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 10
MIN_ITEM = -5
MAX_ITEM = 5
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

# берем только первый мин/макс в списке, если их несколько
min_pos, max_pos = 0, 0

for pos in range(1, len(array)):
    if array[min_pos] > array[pos]:
        min_pos = pos
    if array[max_pos] < array[pos]:
        max_pos = pos

if min_pos == max_pos:
    print('Все числа в списке одинаковы, невозможно посчитать сумму между мин и макс элементами')
else:
    a, b = (min_pos, max_pos) if min_pos < max_pos else (max_pos, min_pos)
    sum_numbers = 0
    for i in range(a + 1, b):
        sum_numbers += array[i]
    print(f'Позиция мин.: {min_pos}, поз макс.: {max_pos}')
    print(f'Сумма равна: {sum_numbers}')
