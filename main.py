import sys, subprocess, colorama
from colorama import Fore, Back

colorama.init(autoreset=True)

CONNECT_LENGTH = 3
BOARD_WIDTH = 3
BOARD_HEIGHT = 3
EMPTY_SYMBOL = '*'
PLAYER_ONE_SYMBOL = 'X'
PLAYER_TWO_SYMBOL = 'O'

which_player = True
board = [[EMPTY_SYMBOL for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]


def draw_board():
    print()
    for i in range(len(board)):
        print('\t ', end= '')
        print(*board[i], sep= ' | ')
        if i+1 != BOARD_WIDTH:
            print('\t', '-'*(3*len(board[0])+1))


def check_board():
    can_place = False
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == EMPTY_SYMBOL:
                can_place = True
                continue
            if CONNECT_LENGTH <= (BOARD_WIDTH-y):
                if board[x][y] == board[x][y+1] and board[x][y] == board[x][y+2]:
                    if board[x][y] == PLAYER_ONE_SYMBOL:
                        return Fore.BLACK + Back.YELLOW + '\n\tPLAYER ONE WINS'
                    elif board[x][y] == PLAYER_TWO_SYMBOL:
                        return Fore.BLACK + Back.YELLOW + '\n\tPLAYER TWO WINS'
            if CONNECT_LENGTH <= (BOARD_HEIGHT-x):
                if board[x][y] == board[x+1][y] and board[x][y] == board[x+2][y]:
                    if board[x][y] == PLAYER_ONE_SYMBOL:
                        return Fore.BLACK + Back.YELLOW + '\n\tPLAYER ONE WINS'
                    elif board[x][y] == PLAYER_TWO_SYMBOL:
                        return Fore.BLACK + Back.YELLOW + '\n\tPLAYER TWO WINS'
            if CONNECT_LENGTH <= (BOARD_WIDTH-y) and CONNECT_LENGTH <= (BOARD_HEIGHT-x):
                if board[x][y] == board[x+1][y+1] and board[x][y] == board[x+2][y+2]:
                    if board[x][y] == PLAYER_ONE_SYMBOL:
                        return Fore.BLACK + Back.YELLOW + '\n\tPLAYER ONE WINS'
                    elif board[x][y] == PLAYER_TWO_SYMBOL:
                        return Fore.BLACK + Back.YELLOW + '\n\tPLAYER TWO WINS'
            if CONNECT_LENGTH <= y+1 and CONNECT_LENGTH <= (BOARD_HEIGHT-x):
                if board[x][y] == board[x+1][y-1] and board[x][y] == board[x+2][y-2]:
                    if board[x][y] == PLAYER_ONE_SYMBOL:
                        return Fore.BLACK + Back.YELLOW + '\n\tPLAYER ONE WINS'
                    if board[x][y] == PLAYER_TWO_SYMBOL:
                        return Fore.BLACK + Back.YELLOW + '\n\tPLAYER TWO WINS'
    if not can_place:
        return Fore.BLACK + Back.YELLOW + '\n\tNOBODY WINS, DRAW'
    return ''


def take_turn(is_player_one):

    global board, PLAYER_ONE_SYMBOL, PLAYER_TWO_SYMBOL, which_player

    row, column = BOARD_HEIGHT+1, BOARD_WIDTH+1
    while row > BOARD_HEIGHT or column > BOARD_WIDTH or board[row-1][column-1] != EMPTY_SYMBOL:
        title = '\n\tPLAYER ONE TURN' if is_player_one else '\n\tPLAYER TWO TURN'
        print(Fore.BLACK + Back.WHITE + title)
        draw_board()
        pos_choice = input(f'\n\tChoose posistion (1-{BOARD_WIDTH*BOARD_HEIGHT}): ')
        if pos_choice == 'exit':
            return 'exit'
        elif pos_choice == 'restart':
            board = [[EMPTY_SYMBOL for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
            subprocess.run('cls', shell=True)
            print(Fore.BLACK + Back.YELLOW + '\n\tRESTART BOARD')
            which_player = True
            return take_turn(which_player)
        try:
            pos_choice = int(pos_choice)
        except ValueError:
            subprocess.run('cls', shell=True)
            print(Fore.BLACK + Back.RED + '\n\tValErr: Invalid Value')
            row = BOARD_HEIGHT+1
            column = BOARD_WIDTH+1
            continue
        except IndexError:
            subprocess.run('cls', shell=True)
            print(Fore.BLACK + Back.RED + '\n\tInxErr: Invalid Posistion')
        row = (pos_choice // BOARD_WIDTH)+1 if pos_choice%BOARD_WIDTH!=0 else pos_choice // BOARD_WIDTH
        column = pos_choice % BOARD_WIDTH
        if row > BOARD_HEIGHT or column > BOARD_WIDTH:
            subprocess.run('cls', shell=True)
            print(Fore.BLACK + Back.RED + '\n\tInvalid Posistion')
            continue
        if board[row-1][column-1] != EMPTY_SYMBOL:
            subprocess.run('cls', shell=True)
            print(Fore.BLACK + Back.RED + '\n\tOccupied Space')
            continue
    subprocess.run('cls', shell=True)
    board[row-1][column-1] = PLAYER_ONE_SYMBOL if is_player_one else PLAYER_TWO_SYMBOL
    check = check_board()
    if check != '':
        print(Fore.BLACK + Back.YELLOW + f'\n\t{check}')
        draw_board()
        input('\n\tExit: ')
        return 'exit'
    which_player = not which_player
    return ''


def main():
    while True:
        run = take_turn(which_player)
        if run == 'exit':
            break


if __name__ == '__main__':
    main()

