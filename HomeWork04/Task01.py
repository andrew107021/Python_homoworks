# Вычислить число pi c заданной точностью d
# Пример:
# - при d = 3, π = 3.141
#
# формула: pi = sum(n=0, n=inf)( (1 / 16**n) * (4/(8*n + 1) - 2/(8*n + 4) - 1/(8*n + 5) - 1/(8*n + 6)) )


d = int(input('Введите точность: '))
calc_pi = 0
check = 0

for n in range(int(10000)):
    calc_pi += (1 / 16**n) * (4/(8*n + 1) - 2/(8*n + 4) - 1/(8*n + 5) - 1/(8*n + 6))
    if abs(check - calc_pi) < 10**(-d):
        break
    check = calc_pi

print('pi = ', round(calc_pi, d))
