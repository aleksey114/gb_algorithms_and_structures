# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
# для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий,
# чья прибыль ниже среднего.

from collections import defaultdict

company_count = int(input('Введите кол-во компаний: '))
# Все на что хватило фантазии. Показалось что из коллекций только это подойдет к задаче.
# В чате пишут что решать нужно с помощью namedtuple, но в задаче нет требования к сохранению значений
# и кажется это более подходящим использованием навыков из урока и неохота переделывать =)
companies = defaultdict(float)

for _ in range(company_count):
    name = input('Введите название компание: ')
    for i in range(4):  # 4 квартала
        quarter_profit = float(input(f'Введите прибыль за {i + 1} квартал: '))
        companies[name] += quarter_profit

average_profit = sum(companies.values()) / company_count

# Два прохода по списку, зато наглядно. Хотел использовать counter, но показалось что будет перебор.
below_average = [key for key, value in companies.items() if value <= average_profit]
above_average = [key for key, value in companies.items() if value > average_profit]

print(f'Компании, где прибыль ниже среднего: {below_average}')
print(f'Компании, где прибыль выше среднего: {above_average}')
