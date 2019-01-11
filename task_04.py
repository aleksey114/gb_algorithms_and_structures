# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 10
MIN_ITEM = -5
MAX_ITEM = 5
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

number = None  # искомое число
count = 0
for pos, item in enumerate(array):
    if item is not None:  # проверим, не учитывали ли мы это значение уже
        current_count = 1
        for i in range(pos + 1, len(array)):  # нас интересует только правая часть от искомого числа
            if i is None:  # не уверен что эта проверка ускорит алгоритм
                continue
            if item == array[i]:
                current_count += 1
                array[i] = None
        if current_count > count:  # если число встречается чаще, обновим значения
            count = current_count
            number = item

print(number, count)
