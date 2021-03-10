# Задача считается решённой, если в ней использована как минимум одна коллекция из модуля collections.
# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.

from collections import deque
from collections import namedtuple

QUARTERS = 4
Company = namedtuple('Company', ['name', 'quarters', 'profit'])
all_companies = set()

num = int(input('Введите кол-во предприятий: '))
total_profit = 0
for i in range(1, num + 1):
    profit = 0
    quarters = []
    name = input(f'Введите название предприятия {i} : ')

    for j in range(QUARTERS):
        quarters.append(int(input(f'Прибыль за {j + 1}-й квартал: ')))
        profit += quarters[j]

    comp = Company(name=name, quarters=tuple(quarters), profit=profit)
    all_companies.add(comp)
    total_profit += profit

average = total_profit / num


print(f'\nСредняя прибыль = {average}')
print(f'\nПредприятия с прибылью выше среднего: ')
for comp in all_companies:
    if comp.profit > average:
        print(f'Компания {comp.name} заработала {comp.profit}')


print(f'\nПредприятия с прибылью ниже среднего: ')
for comp in all_companies:
    if comp.profit < average:
        print(f'Компания {comp.name} заработала {comp.profit}')



# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.

hex_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

bin_numbers = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
               '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
               'C': 12, 'D': 13, 'E': 14, 'F': 15}


def convert(hex_num):
    deq_hex_num = deque(hex_num.upper())
    return deq_hex_num


def sum_hex(first, second):
    first = first.copy()
    second = second.copy()

    if len(second) > len(first):
        first, second = second, first

    second.extendleft('0' * (len(first) - len(second)))

    result = deque()
    overflow = 0
    for i in range(len(first) -1, -1, -1):
        first_num = bin_numbers[first[i]]
        second_num = bin_numbers[second[i]]

        result_num = first_num + second_num + overflow

        if result_num >= 16:
            overflow = 1
            result_num -= 16
        else:
            overflow = 0

        result.appendleft(hex_numbers[result_num])

    if overflow == 1:
        result.appendleft('1')

    return result


def mult_hex(first, second):
    first = first.copy()
    second = second.copy()

    if len(second) > len(first):
        first, second = second, first

    second.extendleft('0' * (len(first) - len(second)))

    result = deque('0')
    for i in range(len(first) -1, -1, -1):
        second_num = bin_numbers[second[i]]

        spam = deque('0')
        for _ in range(second_num):
            spam = sum_hex(spam, first)

        spam.extend('0' * (len(first) - i - 1))
        result = sum_hex(result, spam)

    return result


a = input('Введите первое число в hex формате (только цифры от 0 до f): ')
b = input('Введите второе число в hex формате (только цифры от 0 до f): ')

a = convert(a)
b = convert(b)

print('A + B =', sum_hex(a, b))
print('A * B =', mult_hex(a, b))

