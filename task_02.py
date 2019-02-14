# Закодируйте любую строку из трех слов по алгоритму Хаффмана.
from collections import Counter

original_string = 'beep boop beer!'
frequency = Counter(original_string)

while len(frequency) > 2:
    two_minimum_frequencies = dict(frequency.most_common()[:-3:-1])
    frequency = frequency - Counter(two_minimum_frequencies)
    lst = list(two_minimum_frequencies.items())
    new_value = lst[0][1] + lst[1][1]
    new_str = lst[0][0] + lst[1][0] if len(lst[0][0]) < len(lst[1][0]) else lst[1][0] + lst[0][0]
    new_frequency = Counter({new_str: new_value})
    frequency = frequency + new_frequency

# получили две строки, это две цепочки элементов двух основных нод от корневого элемента
two_node = list(frequency)
dict_haffman = dict()

# добавляем биты согласно алгоритму Хоффмана
for i in range(2):
    bit_str = str(i) * 2
    dict_haffman[two_node[i][0]] = bit_str
    for j in range(1, len(two_node[i])):

        last_two_bit = ''
        if j + 1 == len(two_node[i]):
            last_two_bit = '1' if i == 0 else '0'
        else:
            last_two_bit = '10' if i == 0 else '01'
        bit_str = bit_str[:-1] + last_two_bit
        dict_haffman[two_node[i][j]] = bit_str

print(original_string)
for ch in list(original_string):
    print(f'{dict_haffman[ch]} ', end=' ')
