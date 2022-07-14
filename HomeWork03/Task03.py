# 3. Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random


def generate_lst():     # генератор списка вещественных чисел
    rnd_lst = []
    for _ in range(10):
        nmb = 10 * random.random()     # диапазон 0...9.(9)
        if 0.3 > random.random():
            nmb = int(nmb)
        rnd_lst.append(round(nmb, random.randint(0, 4)))
    return rnd_lst


# вариант 1 (сомнительный из-за особенностей работы с float)
def fractional(nmb: [int, float]) -> float:
    if abs(float(nmb) - int(nmb)) < 1E-19:
        return 0
    else:
        k = 1
        while nmb * 10**k - int(nmb * 10**k) > 0:
            k += 1
        return (nmb * 10**k) % 10**k / 10**k


some_lst = generate_lst()
print(some_lst)

print('Вариант 1')
n_max = n_min = 0
for i in some_lst:
    num = fractional(i)
    if n_max < num:
        n_max = num
    if n_min > num != 0 or n_min == 0:
        n_min = num

print(f'{n_max} - {n_min} = {n_max - n_min}')


# вариант 2
print('Вариант 2')
print(some_lst)
n_max = n_min = 0
for item in some_lst:
    if isinstance(item, float):
        f_part = (str(item).split('.'))[1]
        num = int(f_part)
        num /= 10**len(str(f_part))
        if n_max < num:
            n_max = num
        if n_min > num != 0 or n_min == 0:
            n_min = num

print(f'{n_max} - {n_min} = {n_max - n_min}')
