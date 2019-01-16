# Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.
# Задача: Определить, какое число в массиве встречается чаще всего.
import cProfile
import random

SIZE = 10000
MIN_ITEM = 0
MAX_ITEM = 100000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


def method_1(lst):
    number = None  # искомое число
    count = 0
    for pos, item in enumerate(lst):
        if item is not None:  # проверим, не учитывали ли мы это значение уже
            current_count = 1
            for i in range(pos + 1, len(lst)):  # нас интересует только правая часть от искомого числа
                if i is None:
                    continue
                if item == lst[i]:
                    current_count += 1
                    lst[i] = None
            if current_count > count:  # если число встречается чаще, обновим значения
                count = current_count
                number = item
    return number


# 100 loops, best of 3: 6.99 msec per loop - 1000
# 100 loops, best of 3: 38.2 msec per loop - 5000
# 100 loops, best of 3: 76.1 msec per loop - 10000
# 100 loops, best of 3: 115 msec per loop - 15000
# cProfile.run('method_1(array)')
# 1    0.006    0.006    0.006    0.006 task_04.py:12(method_1) - 1000
# 1    0.066    0.066    0.066    0.066 task_04.py:12(method_1) - 10000

def method_2(lst, number=None, count=0):
    if len(lst) == 0:
        return number

    current_number = lst[0]
    current_count = 1
    modify_lst = []
    for i in range(1, len(lst)):
        if current_number == lst[i]:
            current_count += 1
        else:
            modify_lst.append(lst[i])

    if current_count > count:
        return method_2(modify_lst, current_number, current_count)
    else:
        return method_2(modify_lst, number, count)


# 100 loops, best of 3: 7.56 msec per loop - 1000
# 100 loops, best of 3: 39.3 msec per loop - 5000
# 100 loops, best of 3: 79.4 msec per loop - 10000
# 100 loops, best of 3: 119 msec per loop - 15000
# cProfile.run('method_2(array)')
# 1000
# 102/1    0.008    0.000    0.011    0.011 task_04.py:37(method_2)
# 47275    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
# 5000
# 102/1    0.044    0.000    0.055    0.055 task_04.py:37(method_2)
# 249568    0.011    0.000    0.011    0.000 {method 'append' of 'list' objects}
# 10000
# 102/1    0.089    0.001    0.112    0.112 task_04.py:37(method_2)
# 496075    0.023    0.000    0.023    0.000 {method 'append' of 'list' objects}


def method_3(lst):
    dict_numbers = {}
    number = None
    count = 0
    for item in lst:
        if item in dict_numbers:
            dict_numbers[item] += 1
        else:
            dict_numbers[item] = 1

        if dict_numbers[item] > count:
            count = dict_numbers[item]
            number = item
    return number

# 100 loops, best of 3: 1.19 msec per loop - 1000
# 100 loops, best of 3: 6.11 msec per loop - 5000
# 100 loops, best of 3: 12.1 msec per loop - 10000
# 100 loops, best of 3: 18.4 msec per loop - 15000
# cProfile.run('method_3(array)')
# 1    0.000    0.000    0.000    0.000 task_04.py:72(method_3) - 1000
# 1    0.001    0.001    0.001    0.001 task_04.py:72(method_3) - 10000


# Замер времени генерации списка, не стал разбираться самостоятельно как исключить автоматом, решил дождаться урока
# Значения не вычитал, просто принял к сведению для выводов.
# python -m timeit -n 100 -s "import random" "array=[random.randint(0,100) for _ in range(5000)]"
# 100 loops, best of 3: 1.06 msec per loop - 1000
# 100 loops, best of 3: 5.37 msec per loop - 5000
# 100 loops, best of 3: 10.7 msec per loop - 10000
# 100 loops, best of 3: 16 msec per loop - 15000


# 1 метод и 2 метод сильно похожи, если копнуть ближе хвостовая рекурсия (2 метод) это тот же 1-ый метод.
# Сложность алгоритов O(n).
# Увеличил диапазон чисел в списке. Потестировал. График зависимости стал немного быстрей подниматься.

# 3 метод показал лучшие результаты. Не ожидал что настолько лучше.
# Попробовал увеличить диапазон случайных значений в списке (чтоб словарь в итоге вышел больше),
# алгоритм совершенно незначительно увеличил время. Отличный алгоритм. Сложность алгоритма O(n)
# Если есть свободная память, определенно этот алгоритм лучший.
# Тем более размер дополнительной памяти можно сразу предположить.

# Методы 1/2 и метод 3 могут возвращат разный ответ из-за разницы алгоритмов, но это будет все так же
# число встречающееся максимальное кол-во раз. Просто с этой же частотой могут встречаться разные числа.
