# Написать два алгоритма нахождения i-го по счёту простого числа.
import math
import cProfile


def method_sieve(position):
    if position == 1:
        return 2
    current_position = 0

    len_coef = 3 if position < 50 else 1.2
    len_sieve = int(position * math.log(position) * len_coef)

    sieve = [i for i in range(len_sieve)]
    sieve[1] = 0
    for i in sieve:
        if not i == 0:
            current_position += 1
            for j in range(i + i, len_sieve, i):
                sieve[j] = 0

        if current_position == position:
            return i


# 100 loops, best of 3: 9.11 usec per loop - 10
# 100 loops, best of 3: 40 usec per loop - 50
# 100 loops, best of 3: 99.8 usec per loop - 100
# 100 loops, best of 3: 165 usec per loop - 150
# 100 loops, best of 3: 236 usec per loop - 200
# 100 loops, best of 3: 305 usec per loop - 250
# 100 loops, best of 3: 1.58 msec per loop - 1000
# cProfile.run('method_sieve(1000)')
# 1    0.001    0.001    0.002    0.002 task_02.py:6(method_sieve) - 1000

def method_division(position):
    if position == 1:
        return 2
    number = 2
    current_position = 1
    while True:
        number += 1

        is_simple_number = True
        for i in range(2, number):
            if number % i == 0:
                is_simple_number = False
                break

        if is_simple_number:
            current_position += 1
        if position == current_position:
            return number

# 100 loops, best of 3: 13.8 usec per loop - 10
# 100 loops, best of 3: 285 usec per loop - 50
# 100 loops, best of 3: 1.25 msec per loop - 100
# 100 loops, best of 3: 3.04 msec per loop - 150
# 100 loops, best of 3: 5.83 msec per loop - 200
# 100 loops, best of 3: 9.7 msec per loop - 250
# 100 loops, best of 3: 210 msec per loop - 1000
# cProfile.run('method_division(1000)')
# 1000
# 1    0.210    0.210    0.210    0.210 task_02.py:36(method_division)
# 1    0.000    0.000    0.210    0.210 {built-in method builtins.exec} - предполагаю это выполнение операции "%"


# Сложность алгоритма с решетом O(n) = n*log(n). Требует память на хранение решета.
# Сложность алгоритма с делением O(n) = n*n*log(n) , доп. память не использует, но медленней.
