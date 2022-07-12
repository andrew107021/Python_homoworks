# Дополнительно:
# Вклад в банке составляет X рублей. Ежегодно он увеличивается на P процентов,
# после чего дробная часть копеек отбрасывается.
# Требуется определить: через сколько лет вклад составит не менее Y рублей.
# Пример:
# 100
# 10
# 200
# Вывод:
# 8
def calculate(money_in, money_out, prc):
    years = 0
    while money_in < money_out:
        money_in += round(money_in, 2) * (prc/100)
        years += 1
    return years


deposit = float(input('Введите сумму вклада: '))
percent = float(input('Введите годовой процент: '))
result = float(input('Введите ожидаемую сумму: '))

print('Лет до достижения желаемого результата:', calculate(deposit, result, percent))

