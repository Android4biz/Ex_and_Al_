import random

# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.

a = [0] * 8

for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            a[j - 2] += 1

for i, item in enumerate(a, start=2):
    print(f'Число {i} кратно {item} чисел')


# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5,
# т. к. именно в этих позициях первого массива стоят четные числа.


SIZE = 10
array = [random.randint(-100, 100) for _ in range(SIZE)]
print(array)

result = []

for i in range(len(array)):
    if array[i] % 2 == 0:
        result.append(i)

print(f'Индексы четных элементов: {result}')


# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.


SIZE = 10
array = [random.randint(-100, 100) for _ in range(SIZE)]
print(array)


idx_min = 0
idx_max = 0

for i in range(SIZE):
    if array[i] < array[idx_min]:
        idx_min = i
    elif array[i] > array[idx_max]:
        idx_max = i

print(f'Min = {array[idx_min]} в ячейке {array[idx_min]}'
      f'\nMax = {array[idx_max]} в ячейке {array[idx_max]}')
array[idx_min], array[idx_max] = array[idx_max], array[idx_min]
print(array)



SIZE = 10
array = [random.randint(0, SIZE // 1.5) for _ in range(SIZE)]
print(array)

num = array[0]
max_frq = 1

for i in range(SIZE - 1):
    frq = 1

    for k in range(i + 1, SIZE):
        if array[i] == array[k]:
            frq += 1
        if frq > max_frq:
            max_frq = frq
            num = array[i]

if max_frq > 1:
    print(f'Число {num} встречается {max_frq} раз')
else:
    print('Все числа уникальны')


# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.


SIZE = 10
array = [random.randint(-100, 100) for _ in range(SIZE)]
print(array)

i = 0
index = -1

while i < SIZE:
    if array[i] < 0 and index == -1:
        index = i
    elif array[i] < 0 and array[i] > array[index]:
        index = i
    i += 1

print(f'Число {array[index]} на позиции {index}')


# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.


SIZE = 10
array = [random.randint(-100, 100) for _ in range(SIZE)]
print(array)


idx_min = 0
idx_max = 0

for i in range(1, SIZE):
    if array[i] < array[idx_min]:
        idx_min = i
    elif array[i] > array[idx_max]:
        idx_max = i

print(array[idx_min], array[idx_max])

if idx_min > idx_max:
    idx_min, idx_max = idx_max, idx_min

summ = 0

for i in range(idx_min + 1, idx_max):
    summ += array[i]

print(summ)


# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

SIZE = 10
array = [random.randint(-100, 100) for _ in range(SIZE)]
print(array)

if array[0] > array[1]:
    min_idx_1 = 0
    min_idx_2 = 1
else:
    min_idx_1 = 1
    min_idx_2 = 0

for i in range(2, SIZE):
    if array[i] < array[min_idx_1]:
        spam = min_idx_1
        min_idx_1 = i

        if array[spam] < array[min_idx_2]:
            min_idx_2 = spam

    elif array[i] < array[min_idx_2]:
        min_idx_2 = i

print(f'Число {array[min_idx_1]} в ячейке {min_idx_1}')
print(f'Число {array[min_idx_2]} в ячейке {min_idx_2}')


# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

M = 5
N = 4
matrix = []

for i in range(N):
    row = []
    summ = 0

    for j in range(M - 1):
        num = int(input(f'Строка {i},  элемент {j}: '))
        summ += num
        row.append(num)

    row.append(summ)
    matrix.append(row)

for line in matrix:
    for item in line:
        print(f'{item:>5}', end='')
    print()


# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

SIZE = 5

matrix = [[random.randint(-100, 100) for _ in range(SIZE)] for _ in range(SIZE)]

for line in matrix:
    print(*line, sep='\t')

max_ = matrix[0][0]

for j in range(SIZE):
    min_ = matrix[0][j]

    for i in range(SIZE):
        if matrix[i][j] < min_:
            min_ = matrix[i][j]

    if min_ > max_:
        max_ = min_

print(f'Max in min: {max_}')