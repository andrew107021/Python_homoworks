# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N. Факториал
# Пример:
# 5! = 120

def fact_cyc(num_in):
    num_out = 1
    for i in range(1, num_in+1):
        num_out *= i
    return num_out


def fact_rec(num_in):
    if num_in == 1:
        return 1
    return num_in * fact_rec(num_in-1)


num = int(input('Введите число: '))

print(f'Решение циклом: {num}! = {fact_cyc(num)}')
print(f'Рекурсивное решение: {num}! = {fact_rec(num)}')
