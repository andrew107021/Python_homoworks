# 1.  Напишите программу, которая принимает на вход вещественное число
#     и показывает сумму его цифр.
#
#     Пример:
#     6782 -> 23
#     0,56 -> 11
number = input('Введите вещественное число: ')

# вариант 1
result = 0
for char in number:
    if char.isdigit():
        result += int(char)

print(f'{number} -> {result}')


# вариант 2. map применяет функцию к каждому элементу итерируемого объекта.
print(number, '->',
      sum(
          list(map(int, number.split('.')[0]))) +
      sum(list(map(int, number.split('.')[1])))
      )
