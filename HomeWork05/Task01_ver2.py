# 1. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая
# ход друг после друга. Первый ход определяется жеребьёвкой. За один
# ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются
# сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) (доп) Подумайте как наделить бота ""интеллектом""
#
#
from random import randint

CANDIES_ON_TABLE = 2021
# CANDIES_ON_TABLE = 121    # testing value
AMT_MAX = 28
names = tuple()
mode = ''
candies = 0


def player(pl_name):
    """human capture"""
    candie_bank = 0
    name = pl_name

    def get_name():
        return name

    def taker():
        global candies
        nonlocal candie_bank
        take_amt = int(input(f'Сколько конфет берёте (0 min, 28 max), {name}? '))
        if take_amt > AMT_MAX or take_amt < 0:
            take_amt = AMT_MAX
        candie_bank += take_amt
        return take_amt
    return taker, get_name  # return functions: taker -> candies amount, get_name -> player name


def intro2():
    print(
        '''
        Играем в конфеты. 
        Полиси: можно взять от 0 до 28 штук.
        Если взять меньше 0 (интересный вариант...) или больше 28,
        считается что взял 28. Поехали.    
    '''
        )

    flag_0 = 1
    global mode
    global names
    while flag_0:
        mode = input('Играем с компьютером или на двоих? (1/2/exit): ')
        if mode == 'exit':
            print('Выход')
            raise SystemExit
        elif mode not in ('1', '2'):
            print('Ошибка ввода.')
        else:
            flag_0 = 0

    if mode == '1':
        names = (
            ai_player2(),
            player(input('Введите имя: ')))
    else:
        names = (
            player(input('Введите имя 1-го игрока: ')),
            player(input('Введите имя 2-го игрока: '))
        )

    game_play2()


def game_play2() -> None:
    """basic logic"""
    global names, candies
    candies = CANDIES_ON_TABLE
    person = randint(0, 1)
    flag = 1
    while flag:
        print(f'Конфет на столе: {candies}')
        num_take = names[person][0]()

        if candies <= 28:
            print(f'{names[person][1]()} забирает {candies} конфет.')
        else:
            print(f'{names[person][1]()} берёт {num_take} конфет.')
        candies -= num_take
        if candies <= 0:
            print(f'{names[person][1]()} победил')
            flag = 0
        person = (person + 1) % 2


def ai_player2() -> tuple:
    """primitive AI"""
    name = 'An Artificial One II'

    def get_name():
        return name

    def taker():
        global candies
        if candies < AMT_MAX:
            return candies
        elif candies - AMT_MAX > 1 and candies < AMT_MAX * 2:
            return candies - 27
        else:
            return AMT_MAX
    return taker, get_name


intro2()
