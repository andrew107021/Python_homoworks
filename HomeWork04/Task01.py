# Вычислить число pi c заданной точностью d
# Пример:
# - при d = 3, π = 3.141
#
# формула: pi = sum(n=0, n=inf)( (1 / 16**n) * (4/(8*n + 1) - 2/(8*n + 4) - 1/(8*n + 5) - 1/(8*n + 6)) )
# import time
# from math import pi

d = int(input('Введите точность: '))
calc_pi = 0
check = 0

for n in range(int(10000)):
    calc_pi += (1 / 16**n) * (4/(8*n + 1) - 2/(8*n + 4) - 1/(8*n + 5) - 1/(8*n + 6))
    if abs(check - calc_pi) < 10**(-d):
        break
    check = calc_pi

print('pi = ', round(calc_pi, d))

#
# own_pi = 1
# check2 = (3*(3**0.5 / 2)) * (1**2 / (1**2 - (1/3)**2))
# const = (3*(3**0.5 / 2))
# start = time.monotonic_ns()
# for k in range(1, 1_000_000_000):
#     own_pi *= (k**2 / (k**2 - (1/3)**2))
#     if abs(pi - own_pi * const) < 10**(-d):
#         break
#     check2 = const * own_pi
# print('own_pi:', (3*(3**0.5 / 2)) * own_pi)
# end = time.monotonic_ns() - start
#
# print(f'end ns: {end}\nend sec: {end/1E9}', sep='')
#
