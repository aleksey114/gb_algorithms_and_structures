# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

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
