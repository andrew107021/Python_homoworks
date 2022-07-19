# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и вывести на экран.

def make_polynomial(m_degree):
    if m_degree <= 0:
        return 'EЯR0R'[::-1]
    import random as rnd
    cfnt = [str(rnd.randint(-100, 100)) for _ in range(m_degree + 1)]
    polynom = [cfnt[i] + f'*x^{i}' for i in range(2, len(cfnt))][::-1] + [cfnt[1] + '*x'] + [cfnt[0]]
    polynom = [mmbr if not mmbr.startswith('1*') else mmbr.replace('1*', '') for mmbr in polynom]
    out_line = ' + '.join([mmbr for mmbr in polynom if not mmbr.startswith('0')])
    out_line = out_line.replace(' + -', ' - ')

    if f'x^{m_degree}' in out_line:     # в уравнении есть член максимальной степени
        return out_line + ' = 0'
    elif m_degree == 1 and 'x' in out_line:     # степень уравнения 1, есть x
        return out_line + ' = 0'
    else:
        return make_polynomial(m_degree)    # пересборка уравнения


if __name__ == '__main__':
    degree = int(input('Введите степень многочлена (целое число больше 0): '))
    print(make_polynomial(degree))

# with open('out_file.txt', 'w') as of:
#     for _ in range(500):
#         poly = (make_polynomial(3))
#         of.write(poly + '\n')
#         print(poly)
#


# count = dict().fromkeys([1, 2, 3, 4, 5, 6, 7, 8, 9])
# for _ in range(500):
#     # print(make_polynomial(degree))
#     poly = (make_polynomial(degree))
#     print(poly)
#     for i_d in range(degree + 1):
#         if f'^{i_d}' in poly:
#             if not count[i_d]:
#                 count[i_d] = 1
#             else:
#                 count[i_d] += 1
# print(count)

