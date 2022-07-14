# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе
# для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# вариант 1
def fib(num):
    fib_posi = [0, 1]
    for i in range(2, num+1):
        fib_posi.append(fib_posi[i-1] + fib_posi[i-2])

    fib_nega = [0, 1]
    for i in range(0, num-1):
        fib_nega.append(fib_nega[i] - fib_nega[i+1])

    return fib_nega[-1:1:-1] + fib_posi


# вариант 2
def fib2(num):
    fib_posi = [0, 1]
    for i in range(2, num+1):
        fib_posi.append(fib_posi[i-1] + fib_posi[i-2])

    fib_nega = []
    for i in range(0, num+1):
        fib_nega.append((fib_posi[i] * (-1)**(i + 1)))

    return fib_nega[-1:1:-1] + fib_posi


print(fib(8))
print(fib2(8))
