#
# TO-DO:
# fix play_move_(direction) functions
# fix check_if_stuck function, it shouldnt return always True, and 104th line saying if not flag is temporary for that reason
#

import random
import os

ALLOWED_MOVES = ['w', 'a', 's', 'd']
flag = False

def print_grid():
    for item in grid:
        for i in item:
            print(f"{i}\t", end='')
        print()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

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

def manual_add_item():
    xy = input("insert a character in xcoord,ycoord format: ")
    xy = [int(i) - 1 for i in xy.split(',')]
    grid[xy[0]][xy[1]] = 2

def play_move_up(arr):
    for i in range(4):
        while True:
            temp_arr = arr
            for j in range(3):
                if arr[j][i] == arr[j + 1][i] or arr[j + 1][i] == 0 or arr[j][i] == 0:
                    arr[j][i] += arr[j + 1][i]
                    arr[j + 1][i] = 0
            if arr == temp_arr:
                break

def play_move_down(arr):
    for i in range(4):
        while True:
            temp_arr = arr
            for j in range(3):
                if arr[j][i] == arr[j + 1][i] or arr[j + 1][i] == 0 or arr[j][i] == 0:
                    arr[j + 1][i] += arr[j][i]
                    arr[j][i] = 0
            if temp_arr == arr:
                break

def play_move_right(arr):
    for i in range(4):
        while True:
            temp_arr = arr
            for j in range(3):
                if arr[i][j] == arr[i][j + 1] or arr[i][j + 1] == 0 or arr[i][j] == 0:
                    arr[i][j + 1] += arr[i][j]
                    arr[i][j] = 0
            if temp_arr == arr:
                break

def play_move_left(arr):
    for i in range(4):
        while True:
            temp_arr = arr
            for j in range(3):
                if arr[i][j] == arr[i][j + 1] or arr[i][j + 1] == 0 or arr[i][j] == 0:
                    arr[i][j] += arr[i][j + 1]
                    arr[i][j + 1] = 0
            if temp_arr == arr:
                break

def check_if_stuck():
    x = 0
    temp_grid = grid
    play_move_up(temp_grid)
    if temp_grid == grid:
        x += 1
    temp_grid = grid
    play_move_down(temp_grid)
    if temp_grid == grid:
        x += 1
    temp_grid = grid
    play_move_left(temp_grid)
    if temp_grid == grid:
        x += 1
    temp_grid = grid
    play_move_right(temp_grid)
    if temp_grid == grid:
        x += 1
    if x == 4:
        return True

def play_input():
    move = input('Input direction: ').lower()
    if len(move) > 1 or move not in ALLOWED_MOVES:
        print('Try again;')
        play_input()
    if move == 'w':
        play_move_up(grid)
    elif move == 's':
        play_move_down(grid)
    elif move == 'd':
        play_move_right(grid)
    elif move == 'a':
        play_move_left(grid)

def main():
    while True:
        clear_screen()
        add_item()
        flag = check_if_stuck
        if not flag:
            print("Game over")
            break
        print_grid()
        play_input()

while True:
    grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    main()
    if input("Do you want to play another game? [y/N] ")!="y":
        break
