from turtle import clear
import numpy as np


grid = [[0, 8, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 1, 0, 0],
        [0, 0, 4, 0, 1, 8, 0, 2, 0],
        [7, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 3, 9, 2, 0, 0],
        [0, 9, 0, 0, 8, 2, 3, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 6, 0, 0, 0]]


def possible(i, j, a, grid):
    row = grid[i]
    col = list()
    box = list()
    for n in range(9):
        col.append(grid[n][j])
    i0 = i//3 * 3
    j0 = j//3 * 3
    for x in range(3):
        for y in range(3):
            box.append(grid[i0+x][j0+y])
    if a not in row and a not in col and a not in box:
        return True
    else:
        return False


def sudoku_solver(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for n in range(1, 10):
                    if possible(i, j, n, grid):
                        grid[i][j] = n
                        sudoku_solver(grid)
                        grid[i][j] = 0
                return
    print(np.matrix(grid))


# for i in range(9):
#     while 0 in grid[i]:
#         sudoku_solver(grid)
#         print(np.matrix(grid))
sudoku_solver(grid)
