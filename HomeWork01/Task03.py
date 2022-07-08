# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится
# эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
text = '''
   II |  I
 _____|_____
  III | IV
      |
'''
print(text)

x_coord = int(input('Введите координату X: '))
y_coord = int(input('Введите координату Y: '))

if x_coord > 0 < y_coord:
    print('Квадрант I')
elif x_coord < 0 < y_coord:
    print('Квадрант II')
elif x_coord < 0 > y_coord:
    print('Квадрант III')
elif x_coord > 0 > y_coord:
    print('Квадрант IV')
elif x_coord == 0 == y_coord:
    print('В начале координат')
elif x_coord == 0:
    if y_coord > 0:
        print('На оси X, выше оси Y')
    else:
        print('На оси X, ниже оси Y')
elif 0 == y_coord:
    if x_coord > 0:
        print('На оси Y, правее оси X')
    else:
        print('На оси Y, левее оси X')
