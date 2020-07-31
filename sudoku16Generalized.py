# Sudoku puzzle solution to solve any sudoku solution.
# (Generalized solution)
import math
import sys

sys.setrecursionlimit(10 ** 6)


def display_grid(array):
    for i in range(len(array)):
        for j in range(len(array)):
            print(array[i][j], end=" ")
        print('\n')


def find_empty_location(array, index):
    for row in range(len(array)):
        for col in range(len(array)):
            if array[row][col] == '.':
                index[0] = row
                index[1] = col
                return True
    return False


def used_in_row(array, row, num):
    for i in range(len(array)):
        if (array[row][i] == num):
            return True
    return False


def used_in_col(array, col, num):
    for i in range(len(array)):
        if (array[i][col] == num):
            return True
    return False


def used_in_box(array, row, col, num):
    for i in range(int(math.sqrt(len(array)))):
        for j in range(int(math.sqrt(len(array)))):
            if (array[i + row][j + col] == num):
                return True
    return False


def is_safe(array, row, col, num):
    return not used_in_row(array, row, str(num)) and not \
        used_in_col(array, col, str(num)) and not \
        used_in_box(array, (row - row % int(math.sqrt(len(array)))), (col - col % int(math.sqrt(len(array)))), str(num))


def solve_sudoku(array):
    index = [0, 0]
    if (not find_empty_location(array, index)):
        return True

    row = index[0]
    col = index[1]

    for num in range(1, len(array)+1):
        if num > 9:
            num = num + 55
            num = chr(num)
        if (is_safe(array, row, col, str(num))):
            array[row][col] = str(num)
            if (solve_sudoku(array)):
                return True
            array[row][col] = '.'
    return False


Hardarray = [
    [".", "9", ".", ".", "2", ".", "3", "8", "A", ".", ".", ".", ".", ".", ".", "."],
    [".", "1", ".", "6", ".", ".", "D", ".", ".", ".", "8", ".", "F", ".", "B", "5"],
    [".", ".", ".", "3", ".", "B", ".", ".", ".", "5", ".", ".", "G", ".", ".", "."],
    ["7", ".", ".", "F", ".", ".", ".", "A", ".", ".", "G", "1", ".", "4", ".", "."],
    ["G", ".", ".", ".", ".", ".", ".", "D", ".", "A", "C", "7", ".", ".", ".", "F"],
    [".", ".", ".", ".", "1", "3", ".", "F", ".", "B", ".", "8", ".", ".", ".", "."],
    ["1", "8", ".", "A", ".", ".", ".", "E", ".", ".", ".", ".", "2", ".", ".", "6"],
    ["5", ".", ".", ".", ".", ".", ".", ".", ".", "D", ".", ".", "E", "G", "4", "1"],
    ["9", ".", ".", ".", "E", ".", ".", ".", "7", "1", ".", ".", ".", "A", ".", "4"],
    [".", ".", ".", ".", ".", ".", "1", ".", ".", "9", ".", "E", "C", ".", "8", "."],
    [".", "2", "C", "D", ".", ".", "7", ".", "4", ".", ".", ".", ".", "E", "5", "."],
    [".", "4", ".", ".", ".", ".", ".", ".", ".", ".", "D", "6", ".", ".", ".", "G"],
    [".", ".", ".", ".", "F", "8", "B", "4", ".", ".", ".", "2", "A", ".", ".", "."],
    ["E", "3", ".", ".", "9", "7", ".", ".", "6", ".", ".", ".", ".", ".", ".", "."],
    [".", "F", "8", "4", ".", ".", "A", ".", ".", ".", "5", ".", "6", ".", ".", "9"],
    [".", ".", ".", ".", ".", "2", ".", "1", "8", ".", ".", "B", ".", ".", ".", "D"]
]

Easyarray = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

if (solve_sudoku(Hardarray)):
    display_grid(Hardarray)
else:
    print("no solution")
