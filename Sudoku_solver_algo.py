size = 9


def print_sol(a):
    for i in range(size):
        for j in range(size):
            print(a[i][j], end=" ")
        print()


def solve(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False

    for x in range(9):
        if grid[x][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False

    return True


def sudoku(grid, row, col):
    if row == size - 1 and col == size:
        return True

    if col == size:
        row += 1
        col = 0

    if grid[row][col] > 0:
        return sudoku(grid, row, col + 1)

    for num in range(1, size + 1):

        if solve(grid, row, col, num):

            grid[row][col] = num
            if sudoku(grid, row, col + 1):
                return True
        grid[row][col] = 0

    return False


question1 = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
             [0, 1, 0, 0, 0, 4, 0, 0, 0],
             [4, 0, 7, 0, 0, 0, 2, 0, 8],
             [0, 0, 5, 2, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 9, 8, 1, 0, 0],
             [0, 4, 0, 0, 0, 3, 0, 0, 0],
             [0, 0, 0, 3, 6, 0, 0, 7, 2],
             [0, 7, 0, 0, 0, 0, 0, 0, 3],
             [9, 0, 3, 0, 0, 0, 6, 0, 4]]

question2 = [[0, 0, 0, 2, 6, 0, 7, 0, 1],
             [6, 8, 0, 0, 7, 0, 0, 9, 0],
             [1, 9, 0, 0, 0, 4, 5, 0, 0],
             [8, 2, 0, 1, 0, 0, 0, 4, 0],
             [0, 0, 4, 6, 0, 2, 9, 0, 0],
             [0, 5, 0, 0, 0, 3, 0, 2, 8],
             [0, 0, 9, 3, 0, 0, 0, 7, 4],
             [0, 4, 0, 0, 5, 0, 0, 3, 6],
             [7, 0, 3, 0, 1, 8, 0, 0, 0]]

# the empty spaces in the sudoku are filled with zeros

if sudoku(question2, 0, 0):
    print_sol(question2)
else:
    print("Solution for this sudoku does not exist")
