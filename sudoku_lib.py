# SUDOKU GENERATION LIBRARY: Clark Dallas Shaeffer. Last updated 24 October 2020.
# generates a random and filled sudoku puzzle of size 9x9 in the form of a 1D list, all digits included.

# digits are filled from left to right, top to bottom; checking rows, columns and subsquares in each iteration.
# When generating a number from a list of numbers from 1 to 9, if a collision occurs,
# the list of numbers from which a number is chosen removes that number.
# There are many cases in which collisions must inevitably occur and the sudoku breaks,
# and must be started from scratch. Therefore, a solvable and true sudoku is made after many attempts, which are traced.

# generateSudoku() is called when a new Sudoku object is created. The catalyst for creating a sudoku and condition checking.
# NOT OPTIMIZED FOR DYNAMIC SUDOKU SIZE. subsquare-related functions need optimization.

import random


# initializes an empty 1D list to individually append digits as found worthy to participate in the puzzle.
# Each element is checked with its current row, column, and subsquare before being appended to the sudoku.
# Thus, a sudoku is finished and returned only when all 81 elements are placed.
# For each new space, a list of numbers from 1 to 9 is declared (or redeclared). An element is chosen randomly from this list.
# If an element shares its row, column, or subsquare with another of the same element, it collides;
# that specific element is removed from the list and a new element is chosen.
# if there are no more elements to choose from the list, the sudoku fails and is reinitialized.
#   return sudoku: 1D list of 81 integers
def generateSudoku():
    tries = 0  # attempts to generate a complete sudoku
    sudoku = []  # 1D list of all sudoku's elements.

    while len(sudoku) < 81:  # while not a full sudoku
        tries += 1
        num_list = list(range(1, 10))
        num = random.choice(num_list)

        while inRow(sudoku, num) or inCol(sudoku, num) or inSquare(sudoku, num):  # if collision
            try:
                num_list.remove(num)
                num = random.choice(num_list)
            except IndexError:
                sudoku = []  # sudoku fails; reinitialize.
        sudoku.append(num)  # if no collision, add to sudoku.
    return sudoku  # return filled sudoku


# prints the sudoku to the console as lists of each individual row.
#   param sudoku: int list
#   see 9x9 sudoku on console
def PrintSudoku(sud):
    newline = '-------------------------------------\n| '
    to_print = newline
    for i in range(len(sud)):
        if i % 9 == 0 and i > 0:
            to_print += '\n' + newline
        if sud[i] == 0:
            to_print += ' '
        else:
            to_print += str(sud[i])
        to_print += ' | '
    to_print += '\n-------------------------------------'
    print(to_print)


# return the current number of rows in the sudoku.
# Starts at 0 and goes to the current row that is of length < size.
#   param sudoku: int list
#   return int: current rows number, 0 <= x <= 8.
def getRows(sud):
    return int(len(sud) / 9)


# return list of elements in current row.
# if row is full, print full row; len mod size is the same as empty. Just check if row count is more.
#   param sudoku: int list
#   param row: getRows()
#   return list: elements at row 'row' from 0 to the current location.
def getRowList(sud, row):
    if int(len(sud) / 9) > row:
        return sud[(row * 9):(row * 9) + (9)]
    else:
        return sud[(row * 9):(row * 9) + (len(sud) % 9)]


# return if a digit is in the current row list.
#   param sudoku: int list
#   param x: element chosen in generateSudoku() from element list.
#   return bool: number collides with another element in the same row.
def inRow(sud, x):
    return x in getRowList(sud, getRows(sud))


# return current column position.
# Starts at 0 and goes to the current column that is of length < size.
#   param sudoku: int list
#   return int: current columns number, 0 <= y <= 8.
def getCols(sud):
    return len(sud) % 9


# return current column from top to current position.
#   param sudoku: int list
#   param col: getCols()
#   return list: elements at column 'col' from 0 to the current location.
def getColList(sud, col):
    colList = []
    for i in range(getRows(sud)):
        colList.append(sud[i * 9 + col])
    return colList


# return if a digit is in the current column list.
#   param sudoku: int list
#   param y: element chosen in generateSudoku() from element list.
#   return bool: number collides with another element in the same column.
def inCol(sud, y):
    return y in getColList(sud, getCols(sud))


# return integer of current square
#   param sudoku: int list
#   return int: current subsquare number, 0 <= x <= 8.
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


# return list of current square up to current position.
#   param sudoku: int list
#   param sq: getSquare()
#   return list: elements at subsquare 'sq', row by row, up to the current location.
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


# return if a digit is in the current square list.
#   param sudoku: int list
#   param z: element chosen in generateSudoku() from element list.
#   return bool: number collides with another element in the same subsquare.
def inSquare(sud, z):
    return z in getSquareList(sud, getSquare(sud))
