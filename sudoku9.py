# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:

# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3
# sub-boxes of the grid.
# Empty cells are indicated by the character '.'.

def display_grid(array):
    for i in range(9):
        for j in range(9):
            print(array[i][j], end=" ")
        print('\n')


def find_empty_location(array, index):
    for row in range(9):
        for col in range(9):
            if array[row][col] == '.':
                index[0] = row
                index[1] = col
                return True
    return False


def used_in_row(array, row, num):
    for i in range(9):
        if (array[row][i] == num):
            return True
    return False


def used_in_col(array, col, num):
    for i in range(9):
        if (array[i][col] == num):
            return True
    return False


def used_in_box(array, row, col, num):
    for i in range(3):
        for j in range(3):
            if (array[i + row][j + col] == num):
                return True
    return False


def is_safe(array, row, col, num):
    return not used_in_row(array, row, str(num)) and not \
        used_in_col(array, col, str(num)) and not \
        used_in_box(array, row - row % 3, col - col % 3, str(num))


def solve_sudoku(array):
    index = [0, 0]
    if (not find_empty_location(array, index)):
        return True

    row = index[0]
    # print("row", row)
    col = index[1]
    # print("col", col)

    for num in range(1, 10):
        if (is_safe(array, row, col, num)):
            array[row][col] = str(num)
            if (solve_sudoku(array)):
                return True
            array[row][col] = '.'
    return False


array = [
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

solve_sudoku(array)
display_grid(array)
