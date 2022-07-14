# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
while True:
    dec_num = int(input('Введите десятичное целое число (или -1 для выхода): '))
    print(dec_num)
    if dec_num == -1:
        break
    bin_num = '0' if dec_num == 0 else ''

    while dec_num:
        bin_num = str(dec_num % 2) + bin_num
        dec_num //= 2

    print(int(bin_num, 2), '->', bin_num)
