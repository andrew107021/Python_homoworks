
# Напишите программу, которая принимает на вход координаты
# двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

fst_x = float(input('Введите координату X точки A: '))
fst_y = float(input('Введите координату Y точки A: '))
sec_x = float(input('Введите координату X точки B: '))
sec_y = float(input('Введите координату Y точки B: '))

delta_x = max(fst_x, sec_x) - min(fst_x, sec_x)
delta_y = max(fst_y, sec_y) - min(fst_y, sec_y)
distance = (delta_x ** 2 + delta_y ** 2) ** 0.5
print(f'Расстояние между A и B: {round(distance, 2)}')
