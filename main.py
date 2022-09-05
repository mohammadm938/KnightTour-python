import os
from time import sleep


N = int(input("enter N*N number : "))


def create_board():
    cheese_board = []
    for i in range(N):
        cheese_board.append([0 for j in range(N)])
    return cheese_board


def create_sec_board():
    cheese_board = []
    for i in range(N):
        cheese_board.append(['♘' for j in range(N)])
    return cheese_board


CHESS_BOARD = create_board()
CHESS_BOARD_SHOW = create_sec_board()
CHESS_BOARD[0][0] = 1


def print_board(cheese_board):
    for i in range(N):
        for j in range(N):
            print(cheese_board[i][j], end=" ")
        print("\n")


def get_possibilities(x, y):
    pos_x = (2, 1, 2, 1, -2, -1, -2, -1)
    pos_y = (1, 2, -1, -2, 1, 2, -1, -2)
    possibilities = []
    for i in range(8):
        if x+pos_x[i] >= 0 and x+pos_x[i] <= (N-1) and y+pos_y[i] >= 0 and y+pos_y[i] <= (N-1) and CHESS_BOARD[x+pos_x[i]][y+pos_y[i]] == 0:
            possibilities.append([x+pos_x[i], y+pos_y[i]])

    return possibilities


def solve():
    counter = 2
    x = 0
    y = 0
    number = N*N-1
    for i in range(number):
        pos = get_possibilities(x, y)
        minimum = pos[0]
        for p in pos:
            if len(get_possibilities(p[0], p[1])) <= len(get_possibilities(minimum[0], minimum[1])):
                minimum = p
        x = minimum[0]
        y = minimum[1]
        CHESS_BOARD[x][y] = counter
        counter += 1


def animatinig():
    counter = 1
    number = N*N
    while counter <= number:
        print_board(CHESS_BOARD_SHOW)
        for idxi, i in enumerate(CHESS_BOARD):
            for idxj, j in enumerate(i):
                if j == counter:
                    os.system("clear")
                    CHESS_BOARD_SHOW[idxi][idxj] = '♞'
                    print_board(CHESS_BOARD_SHOW)
                    sleep(0.25)
                    counter += 1


solve()
print('animating ...')
animatinig()
