# Задайте натуральное число N. Напишите программу, которая составит список
# простых делителей числа N. (1 - составное число)

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    limit = int(num**0.5) + 1
    for divider in range(3, limit, 2):
        if num % divider == 0:
            return False
    return True


natural_n = int(input('Введите натуральное число N: '))
prime_list = []

for i in range(1, natural_n+1):
    if natural_n % i == 0 and is_prime(i):
        prime_list.append(i)

print(f'Список простых делителей {natural_n}:\n', prime_list, sep='')
