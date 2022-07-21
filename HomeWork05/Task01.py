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


def two_players():
    names = ('First', 'Second')
    person = 0
    candies = CANDIES_ON_TABLE
    flag = 1

    print(
        '''
        Number of candies one may take is 0 to 28 pieces.
        You take more then 28 or less then 0 -- You take 28 =). 
    '''
    )

    while flag:
        print(f'Amount of candies: {candies}')
        num_take = int(input(f'How much candies you want to take (0 min, 28 max),{names[person]}? '))
        if num_take > 28 or num_take < 0:
            num_take = AMT_MAX
        print(f'{names[person]} takes {num_take} candies.')
        candies -= num_take
        if candies <=0:
            flag = 0
        person = (person + 1) % 2

    print(f'{names[person]} wins')


def game_play() -> None:
    """basic logic"""
    global names
    candies = CANDIES_ON_TABLE
    person = randint(0, 1)
    flag = 1
    while flag:
        print(f'Конфет на столе: {candies}')
        if person:
            num_take = human()
            if num_take > 28 or num_take < 0:
                num_take = AMT_MAX
        else:
            num_take = ai_player(candies)
        print(f'{names[person]} берёт {num_take} конфет.')
        candies -= num_take
        if candies <= 0:
            print(f'{names[person]} победил')
            flag = 0
        person = (person + 1) % 2


def ai_player(candies: int) -> int:
    """primitive AI"""
    if candies < 28:
        return candies
    elif candies - 28 > 1 and candies < 28 * 2:
        return candies - 27
    else:
        return 28


def human() -> int:
    """human capture"""
    global names
    return int(input(f'Сколько конфет берёте (0 min, 28 max), {names[1]}? '))


print(
    '''
    Играем в конфеты. 
    Полиси: можно взять от 0 до 28 штук.
    Если взять меньше 0 (интересный вариант...) или больше 28,
    считается что взял 28. Поехали.    
'''
    )

names = ('An artificial one', input('Enter name: '))

game_play()
