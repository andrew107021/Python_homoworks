number = int(input('Введите номер столбика: '))
fib_num = [0, 1]

for i in range(1, number):
    fib_num.append(fib_num[i-1] + fib_num[i])

print(fib_num[number])

# let's test connection to git via ssh-key security

