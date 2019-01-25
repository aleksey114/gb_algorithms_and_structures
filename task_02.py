# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
# элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’]
# и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque
import string

# 16-тиричная система счисления. в теории можно понинизить =) не проверял
NS = 16
ns_deq = deque(string.hexdigits[:NS].upper())
ns_pos = {item: pos for pos, item in enumerate(ns_deq)}  # словарь позиций элементов NS системы счислений


def simple_sum(a, b):
    """
    сложение двух элементов счисления
    возвращает очередь из двух элементов [элемент разряда выше, элемент текущего разряда]
    элемент разряда выше может быть либо система_счисления[0], либо система_счисления[1]
    """
    temp_ns_deq = ns_deq.copy()
    move = ns_pos[a] + ns_pos[b]
    temp_ns_deq.rotate(-1 * move)
    current_bit = temp_ns_deq.popleft()
    result_deq = deque([ns_deq[0]] + [current_bit] if move < NS else [ns_deq[1]] + [current_bit])
    return result_deq


def modify_data(a, b):
    """
    модифицирует числа
    дополняет значениями из системы_счисления[0] спереди, числа с меньшей длиной, до совпадения длин
    """
    mod_a, mod_b = deque(a), deque(b)
    if len(a) > len(b):
        mod_b.extendleft([ns_deq[0]] * (len(a) - len(b)))
    else:
        mod_a.extendleft([ns_deq[0]] * (len(b) - len(a)))
    return mod_a, mod_b


def sum_numbers(a, b):
    a, b = modify_data(a, b)
    result = deque()
    while len(a) > 0:
        ai, bi = a.pop(), b.pop()  # ai, bi элементы счисления чисел a и b с меньшим разрядом
        sum_ai_bi = deque(simple_sum(ai, bi))
        if len(result) == 0:
            result.extend(sum_ai_bi)
        else:
            # вычисление значения текущего разряда
            sum_current_digit = simple_sum(result.popleft(), sum_ai_bi.pop())
            result.appendleft(sum_current_digit.pop())
            # вычисления значения разряда выше текущего
            sum_next_digit = simple_sum(sum_current_digit.pop(), sum_ai_bi.pop())
            result.appendleft(sum_next_digit.pop())
    # приведение к нормальному виду, наибольший разряд "нулевой"
    last_left = result.popleft()
    if not last_left == ns_deq[0]:
        result.appendleft(last_left)
    return result


def multi_numbers(a, b):
    result = deque(ns_deq[0])
    digit_number = 0  # разряд текущего числа
    a, b = modify_data(a, b)
    while len(b) > 0:
        count_sum = ns_pos[b.pop()]  # берем поочереди элементы из числа b в порядке увеличения разряда
        temp_a = a.copy()
        # сдвинем разряд, если необходимо
        temp_a.extend([ns_deq[0]] * digit_number)
        # число a складываем с результатом несколько раз
        # кол-во сложений зависит от индекса элемента счисления
        for _ in range(count_sum):
            result = sum_numbers(result.copy(), temp_a)
        digit_number += 1
    return result


if __name__ == '__main__':
    a = list((input('Введите первое число: ')).upper().strip())
    b = list((input('Введите второе число: ')).upper().strip())
    print(sum_numbers(a, b))
    print(multi_numbers(a, b))
