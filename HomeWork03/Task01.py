# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт
# сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from random import randint

some_lst = [randint(0, 10) for _ in range(10)]
result = 0

for i in range(1, len(some_lst), 2):
    result += some_lst[i]

print(some_lst)
print(result)
