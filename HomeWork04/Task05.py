# 35. **(Доп)**. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
from Task04 import make_polynomial


def poly_parse(poly_dict: dict, in_line: str) -> dict:
    if poly_dict == {}:
        poly_dict[1] = 0
        poly_dict[0] = 0
    polynome = in_line.rstrip(' = 0\n').replace(' - ', ' -').replace(' + ', ' ').split()
    print(' + '.join(polynome).replace('+ -', '- ') + ' = 0')
    for item in polynome:
        if '^' in item and int(item.split('^')[1]) not in poly_dict.keys():
            poly_dict[int(item.split('^')[1])] = 0
    for item in polynome:
        if '^' in item:
            if '*' in item:
                poly_dict[int(item.split('^')[1])] += int(item.split('*')[0])
            else:
                poly_dict[int(item.split('^')[1])] += 1
        elif 'x' in item and '*' in item:
            poly_dict[1] += int(item.split('*')[0])
        elif item == 'x':
            poly_dict[1] += 1
        else:
            poly_dict[0] += int(item)
    return poly_dict


while True:
    degree_1 = int(input('Введите степень 1-го многочлена (целое число больше 0): '))
    degree_2 = int(input('Введите степень 2-го многочлена (целое число больше 0): '))
    if degree_1 > 0 and degree_2 > 0:
        break
    else:
        print('Степени должны быть больше 0')

with open('poly_01.txt', 'w') as out_f:
    out_f.write(make_polynomial(degree_1) + '\n')

with open('poly_02.txt', 'w') as out_f:
    out_f.write(make_polynomial(degree_2) + '\n')


common_dict = {}
with open('poly_01.txt', 'r') as in_f:
    poly_one = in_f.read()
    common_dict = poly_parse(common_dict, poly_one)

with open('poly_02.txt', 'r') as in_f:
    poly_one = in_f.read()
    common_dict = poly_parse(common_dict, poly_one)

result2 = ''
for key, val in sorted(common_dict.items(), reverse=True):
    if key == 0:
        result2 += f'{str(val)}'
    elif key < 2:
        result2 += f'{str(val)}*x + '
    else:
        result2 += f'{str(val)}*x^{str(key)} + '

result2 = result2.rstrip(' +').replace('+ -', '- ') + ' = 0'
print('='*80 + '\n' + result2)
with open('poly_result.txt', 'w') as out_f:
    out_f.write(result2 + '\n')
