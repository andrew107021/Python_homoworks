# 3. Задана последовательность натуральных чисел, завершающаяся числом 0.
# Требуется определить значение второго по величине элемента в этой последовательности,
# то есть элемента, который будет наибольшим,
# если из последовательности удалить наибольший элемент.

# Пример:
# 1
# 7
# 9
# 0
# Вывод:
# 7
#
#
#
#
#
#
#
#
# Вариант 1
def task03_1():
    print('Вариант 1')
    f_max = [0, 0]
    flag = 1

    while flag:
        num = input('Введите натуральное число (0 -- конец ввода): ')
        if not num.isnumeric() or int(num) < 0:
            print('Ошибка ввода')
        else:
            num = int(num)
            if f_max == [0, 0]:
                f_max = [num, num]
            if f_max[0] < num < f_max[1]:
                f_max[0] = num
            elif f_max[1] < num:
                f_max[0], f_max[1] = f_max[1], num
            elif num == 0:
                flag = 0

    if f_max == [0, 0]:
        print('Пустая последовательность.')
    else:
        print('Второй наибольший:', f_max[1])


# Вариант 2
def task03_2():
    print('Вариант 2')
    f_max = []
    flag = 1

    while flag:
        num = input('Введите натуральное число (0 -- конец ввода): ')
        if not num.isnumeric() or int(num) < 0:
            print('Ошибка ввода')
        elif num == '0':
            flag = 0
        else:
            num = int(num)
            f_max.append(num)
    if len(f_max) >= 2:
        print('Второй наибольший:', sorted(f_max)[-2])
    elif len(f_max) == 1:
        print('Второй наибольший:', f_max[0])
    else:
        print('Пустая последовательность.')


task03_1()
task03_2()
