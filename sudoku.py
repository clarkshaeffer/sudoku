import random


def main():
    found = False
    tries = 0
    # main.counter += 1

    # starting with just 9x9.

    sudoku = []  # 1D list of all sudoku's elements.

    while len(sudoku) < 81:
        tries += 1
        num_list = list(range(1, 10))
        num = random.choice(num_list)

        while inRow(sudoku, num) or inCol(sudoku, num) or inSquare(sudoku, num):
            try:
                num_list.remove(num)
                num = random.choice(num_list)
            except IndexError:
                sudoku = []
        sudoku.append(num)
    PrintSudoku(sudoku)
    print("tries: " + str(tries))


def PrintSudoku(sud):
    rows = getRows(sud)
    for i in range(rows + 1):
        print(getRowList(sud, i))


def getRows(sud):
    # get the current number of rows in the sudoku. Starts at 0 and goes to the current row that is of length < size.
    return int(len(sud) / 9)


def getRowList(sud, row):
    # get list of elements in current row.
    # if row is full, print full row; len mod size is the same as empty. Just check if row count is more.
    if int(len(sud) / 9) > row:
        return sud[(row * 9):(row * 9) + (9)]
    else:
        return sud[(row * 9):(row * 9) + (len(sud) % 9)]


def inRow(sud, x):
    return x in getRowList(sud, getRows(sud))


def getCols(sud):
    return len(sud) % 9


def getColList(sud, col):
    colList = []
    for i in range(getRows(sud)):
        colList.append(sud[i * 9 + col])
    return colList


def inCol(sud, y):
    return y in getColList(sud, getCols(sud))


def getSquare(sud):
    if getRows(sud) <= 2:
        if getCols(sud) <= 2:
            return 0
        elif getCols(sud) >= 3 and getCols(sud) <= 5:
            return 1
        elif getCols(sud) >= 6 and getCols(sud) <= 8:
            return 2
    elif getRows(sud) >= 3 and getRows(sud) <= 5:
        if getCols(sud) <= 2:
            return 3
        elif getCols(sud) >= 3 and getCols(sud) <= 5:
            return 4
        elif getCols(sud) >= 6 and getCols(sud) <= 8:
            return 5
    elif getRows(sud) >= 6 and getRows(sud) <= 8:
        if getCols(sud) <= 2:
            return 6
        elif getCols(sud) >= 3 and getCols(sud) <= 5:
            return 7
        elif getCols(sud) >= 6 and getCols(sud) <= 8:
            return 8


def getSquareList(sud, sq):
    rows = getRows(sud)
    cols = getCols(sud)
    squareList = []
    if sq == 0:
        for i in range(len(sud)):
            if int(i / 9) <= 2:
                if i % 9 <= 2:
                    squareList.append(sud[i])
    elif sq == 1:
        for i in range(len(sud)):
            if int(i / 9) <= 2:
                if i % 9 >= 3 and i % 9 <= 5:
                    squareList.append(sud[i])
    elif sq == 2:
        for i in range(len(sud)):
            if int(i / 9) <= 2:
                if i % 9 >= 6 and i % 9 <= 8:
                    squareList.append(sud[i])
    elif sq == 3:
        for i in range(len(sud)):
            if int(i / 9) >= 3 and int(i / 9) <= 5:
                if i % 9 <= 2:
                    squareList.append(sud[i])
    elif sq == 4:
        for i in range(len(sud)):
            if int(i / 9) >= 3 and int(i / 9) <= 5:
                if i % 9 >= 3 and i % 9 <= 5:
                    squareList.append(sud[i])
    elif sq == 5:
        for i in range(len(sud)):
            if int(i / 9) >= 3 and int(i / 9) <= 5:
                if i % 9 >= 6 and i % 9 <= 8:
                    squareList.append(sud[i])
    elif sq == 6:
        for i in range(len(sud)):
            if int(i / 9) >= 6 and int(i / 9) <= 8:
                if i % 9 <= 2:
                    squareList.append(sud[i])
    elif sq == 7:
        for i in range(len(sud)):
            if int(i / 9) >= 6 and int(i / 9) <= 8:
                if i % 9 >= 3 and i % 9 <= 5:
                    squareList.append(sud[i])
    elif sq == 8:
        for i in range(len(sud)):
            if int(i / 9) >= 6 and int(i / 9) <= 8:
                if i % 9 >= 6 and i % 9 <= 8:
                    squareList.append(sud[i])
    return squareList


def inSquare(sud, z):
    return z in getSquareList(sud, getSquare(sud))


main()
