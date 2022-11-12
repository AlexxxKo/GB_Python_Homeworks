# Создайте программу для игры с конфетами человек против человека.
# Условие задачи:
# На столе лежит 2021 конфета. Играют два игрока,
# делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

from random import randint


def init(n: int) -> dict:
    dct = {}
    if n == 1:
        dct['player1'] = input('Введите имя первого игрока: ')
        dct['player2'] = input('Введите имя второго игрока: ')
    elif n == 2:
        dct['player1'] = input('Введите ваше имя: ')
        dct['player2'] = 'Начинающий Бот'
    else:
        dct['player1'] = input('Введите ваше имя: ')
        dct['player2'] = 'Опытный Бот'
    dct['candiesNumber'] = 99
    dct['move'] = randint(0, 2)
    whose_move(dct)

    dct['mode'] = n

    return dct


def whose_move(dct: dict) -> dict:
    if dct['move']:
        dct['playerMove'] = dct['player2']
    else:
        dct['playerMove'] = dct['player1']
    return dct


def gameFriend(dct: dict) -> str:
    print(f'Начинает {dct["playerMove"]}')

    while dct['candiesNumber'] > 28:
        if dct['mode'] == 1:
            candies_number = get_take_candies(dct['playerMove'])
        elif dct['mode'] == 2:
            if dct['move']:
                candies_number = little_comp()
            else:
                candies_number = get_take_candies(dct['playerMove'])
        else:
            if dct['move']:
                candies_number = big_comp(dct['candiesNumber'])
            else:
                candies_number = get_take_candies(dct['playerMove'])

        dct['candiesNumber'] -= candies_number
        dct['move'] = not dct['move']
        whose_move(dct)

        print(
            f'Осталось {dct["candiesNumber"]} конфет.\n\nХод перешёл к {dct["playerMove"]}\n')
    print(f'{dct["playerMove"]} выиграл')


def get_take_candies(playerName: str) -> int:
    n = int(
        input(f'{playerName}, сколько конфет вы хотите взять (от 1 до 28)? '))
    while n < 1 or n > 28:
        n = int(input('Нужно взять от 1 до 28 конфет. Попробуйте ещё раз: '))
    return n


def select_game_mode():
    print('1 - Игра с другом')
    print('2 - Игра с ботом')
    print('3 - Игра с умным ботом')
    x = int(input('С кем играем? '))
    while not 0 < x < 4:
        x = int(input('Соперник сбежал. С кем играем? '))
    gameFriend(init(x))


def little_comp() -> int:
    n = randint(1, 29)
    return n


def big_comp(candies_num):
    rest = candies_num % 28
    if rest == 0:
        n = 27
    elif rest == 1:
        n = randint(1, 29)
    else:
        n = rest - 1
    return n


select_game_mode()
