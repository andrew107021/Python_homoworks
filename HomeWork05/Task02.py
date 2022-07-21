# 2. Создайте программу для игры в "Крестики-нолики".
from random import randint
BOARD_SZ = 3    # board size
used = []       # global list of used places


def tic_tac_toe() -> None:
    """basic logic"""
    board = [['_' for _ in range(BOARD_SZ)] for _ in range(BOARD_SZ)]
    player = randint(0, 1)      # who starts
    marker = ('0', 'X')

    while True:     # play until finish
        def board_print() -> None:
            for row_lst in board:
                print(*row_lst, sep=' | ')
                print()

        def fill(mark) -> None:
            """place a mark"""
            y, x = player_x(mark)
            board[x][y] = mark

        def checker2() -> None:
            """check if there is a winner or board is over"""
            flag = 0
            out = ('XXX', '000')    # finish condition
            if board[0][0] + board[0][1] + board[0][2] in out:          # 1
                flag = 1
            elif board[1][0] + board[1][1] + board[1][2] in out:        # 2
                flag = 1
            elif board[2][0] + board[2][1] + board[2][2] in out:        # 3
                flag = 1

            elif board[0][0] + board[1][0] + board[2][0] in out:        # 4
                flag = 1
            elif board[0][1] + board[1][1] + board[2][1] in out:        # 5
                flag = 1
            elif board[0][2] + board[1][2] + board[2][2] in out:        # 6
                flag = 1

            elif board[0][0] + board[1][1] + board[2][2] in out:        # 7
                flag = 1
            elif board[2][0] + board[1][1] + board[0][2] in out:        # 8
                flag = 1

            if flag:
                board_print()
                print(f'Game over. Игрок {marker[player]} победил.')
                raise SystemExit
            if len(used) >= 6:
                board_print()
                print(f'Game over. Места закончились.{used}')
                raise SystemExit

        board_print()
        fill(marker[player])
        checker2()
        player = (player + 1) % 2   # choose player 0 or 1


def player_x(mark: str) -> tuple[int, int]:
    """player input"""
    print(f'Ход игрока {mark}')
    while True:
        try:
            x, y = map(int, input('Введите координаты через запятую (x,y): ').replace(' ', '').split(','))
        except ValueError:
            print('Ошибка ввода.')
        else:
            x -= 1
            y -= 1
            if (x, y) in used:
                print('Уже занято')
            elif x > BOARD_SZ-1 or y > BOARD_SZ-1 or x < 0 or y < 0:
                print('Координаты за пределами доски.')
            else:
                used.append((x, y))
                return x, y


if __name__ == '__main__':
    tic_tac_toe()
