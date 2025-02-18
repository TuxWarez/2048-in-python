import random
import os

grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
ALLOWED_MOVES = ['w', 'a', 's', 'd']

def print_grid():
    for item in grid:
        for i in item:
            print(f"{i}\t", end='')
        print()
        print()

def check_if_free(num):
    x = random.randint(0, 3)
    y = random.randint(0, 3)
    if grid[x][y] != 0:
        check_if_free(num)
    grid[x][y] = num
    return grid

def add_item():
    for i in range(2):
        if random.randint(0, 100) < 90:
            check_if_free(2)
        else:
            check_if_free(4)

def play_move_up():
    for i in range(4):
        for j in range(3):
            if grid[j][i] == grid[j + 1][i] or grid[j + 1][i] == 0 or grid[j][i] == 0:
                grid[j][i] += grid[j + 1][i]
                grid[j + 1][i] = 0

def play_move_down():
    for i in range(4):
        for j in range(3):
            if grid[j][i] == grid[j + 1][i] or grid[j + 1][i] == 0 or grid[j][i] == 0:
                grid[j + 1][i] += grid[j][i]
                grid[j][i] = 0

def play_move_right():
    for i in range(4):
        for j in range(3):
            if grid[i][j] == grid[i][j + 1] or grid[i][j + 1] == 0 or grid[i][j] == 0:
                grid[i][j + 1] += grid[i][j]
                grid[i][j] = 0

def play_move_left():
    for i in range(4):
        for j in range(3):
            if grid[i][j] == grid[i][j + 1] or grid[i][j + 1] == 0 or grid[i][j] == 0:
                grid[i][j] += grid[i][j + 1]
                grid[i][j + 1] = 0

def play_input():
    move = input('Input direction:').lower()
    if len(move) > 1 or move not in ALLOWED_MOVES:
        print('Try again;')
        play_input()
    if move == 'w':
        play_move_up()
    elif move == 's':
        play_move_down()
    elif move == 'd':
        play_move_right()
    elif move == 'a':
        play_move_left()


while True:
    os.system('clear')
    add_item()
    print_grid()
    play_input()
