# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

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
