# 3. Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
import random as rnd


def generate_lst(size: int) -> list:
    rnd_lst = []
    for _ in range(size):
        nmb = round(-10 + 20 * rnd.random(), rnd.randint(0, 2))
        if 0.3 > rnd.random():
            nmb = int(nmb)
        if 0.3 > rnd.random():
            nmb = str(nmb)
        rnd_lst.append(nmb)

    return rnd_lst


some_list = generate_lst(10_000)

# вариант 1
unique_list = []

for item in some_list:
    if some_list.count(item) == 1:
        unique_list.append(item)

print(f'Неповторяющиеся элементы ({len(unique_list)} шт.):', unique_list)

# вариант 2 (быстрее)
unique_list2 = []

for item in set(some_list):
    if some_list.count(item) == 1:
        unique_list2.append(item)

print(f'Неповторяющиеся элементы ({len(unique_list2)} шт.):', unique_list2)


"""
# проверка
def sorting(in_list: list) -> list:
    print(in_list)
    ints = []
    nonints = []
    strings = []
    for item in in_list:
        if isinstance(item, int):
            ints.append(item)
        elif isinstance(item, float):
            nonints.append(item)
        elif isinstance(item, str):
            strings.append(item)
    ints = sorted(ints)
    nonints = sorted(nonints)
    strings = sorted(strings)
    out_lst = ints + nonints + strings
    return out_lst


print('check: ', sorting(unique_list) == sorting(unique_list2))
# print('fin: ', sorting(unique_list))
# print('fin: ', sorting(unique_list2))
"""