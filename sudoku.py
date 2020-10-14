import random
# import numpy as np
from itertools import chain
import gtimer as gt


# tries = 0


def main():
    main.counter += 1
    size = 9
    square_size = int(size ** (1/2))
    num_list = list(range(1, size + 1))
    # init
    sudoku = []
    num_count = 0
    for i in range(size):
        line = []
        sudoku.append(line)

    # create sudoku!
    # print('creating...')
    # sudoku[0][0] = random.randint(1, size)
    for i in range(size):
        while len(sudoku[i]) < size and num_count < size**2:
            # num = random.randint(1, size)
            try:
                # get random number from possible random numbers not yet tried
                num = random.choice(num_list)
            except IndexError:
                # if all numbers have been tried, a number can't be taken from an empty list. Error and exit.

                # print('Generation error: ran out of numbers to choose from')

                main()

                # exit()
            # refresh match
            match = False

            # print('i: ' + str(i))
            # print("num: " + str(num))
            # PrintSudoku(sudoku, size)

            # not the same row
            for j in range(len(sudoku[i])):
                if num == sudoku[i][j]:
                    # print('same row')
                    match = True

            # if not the same row until now
            if not match:
                # not the same column
                for j in range(i):
                    # print('j: ' + str(j) +
                    #   '\tlen(sudoku[i]): ' + str(len(sudoku[i])))
                    if num == sudoku[j][len(sudoku[i])]:
                        # print('same col')
                        match = True

            # if not same row nor column
            if not match:
                # not the same square
                square = getSquare(sudoku, i, square_size, num_count)
                # print('square: ' + str(square))
                square_list = getSquareList(
                    sudoku, i, square_size, square, num_count)
                if num in square_list:
                    # print('same square')
                    match = True

            # if not in same row, column nor square: new number! Add to the sudoku, and reset the choices list
            if not match:
                # print()
                # print("SQUARE LIST:")
                # print(square_list)
                # print("END SQUARE LIST")
                # print()
                # add to sudoku
                sudoku[i].append(num)
                # print(str(num) + " placed at value " +
                #   str(i) + ", " + str(len(sudoku[i]) - 1))
                # refresh the random number list, for next number to choose again
                num_list = list(range(1, size + 1))
                num_count += 1
                # print()
            else:
                # remove the random number from the list, to not choose again.
                if num in num_list:
                    num_list.remove(num)
                # else:
                    # print(str(num) + " not in list")

    PrintSudoku(sudoku, size)
    print("tries: " + str(main.counter))
    # exit()


def PrintSudoku(sud, size):
    for i in range(size):
        print(sud[i])


def getSquare(sud, row, square_size, num_count):
    # square_nums = []
    # print("row length: " + str(len(sud[row])))
    # if len(sud[row]) > 0 and row > 0:

    # FOR LATER OPTIMIZATION. USE DIVISION OF CURRENT COUNT AND FULL DIMENSIONS AND % TO ISOLATE SQUARE.
    # full_size = square_size ** 2
    # if num_count / full_size < square_size:

    if row / square_size < 1:
        if (len(sud[row])) / square_size < 1:
            # for i in range(0 * (square_size), 1 * (square_size)):
            #     for j in range(0 * (square_size), 1 * (square_size)):
            #         square_nums.append(sud[i][j])
            # return square_nums
            return 0
        elif (len(sud[row])) / square_size >= 1 and (len(sud[row])) / square_size < 2:
            # for i in range(0 * (square_size), 1 * (square_size)):
            #     for j in range(1 * (square_size), 2 * (square_size)):
            #         square_nums.append(sud[i][j])
            # return square_nums
            return 1
        else:
            # for i in range(0 * (square_size), 1 * (square_size)):
            #     for j in range(2 * (square_size), 3 * (square_size)):
            #         square_nums.append(sud[i][j])
            # return square_nums
            return 2
    elif row / square_size >= 1 and row / square_size < 2:
        if (len(sud[row])) / square_size < 1:
            # for i in range(1 * (square_size), 2 * (square_size)):
            #     for j in range(0 * (square_size), 1 * (square_size)):
            #         square_nums.append(sud[i][j])
            # return square_nums
            return 3
        elif (len(sud[row])) / square_size >= 1 and (len(sud[row])) / square_size < 2:
            # for i in range(1 * (square_size), 2 * (square_size)):
            #     for j in range(1 * (square_size), 2 * (square_size)):
            #         square_nums.append(sud[i][j])
            # return square_nums
            return 4
        else:
            # for i in range(1 * (square_size), 2 * (square_size)):
            #     for j in range(2 * (square_size), 3 * (square_size)):
            #         square_nums.append(sud[i][j])
            # return square_nums
            return 5
    else:
        if (len(sud[row])) / square_size < 1:
            # for i in range(2 * (square_size), 3 * (square_size)):
            #     for j in range(0 * (square_size), 1 * (square_size)):
            #         square_nums.append(sud[i][j])
            # return square_nums
            return 6
        elif (len(sud[row])) / square_size >= 1 and (len(sud[row])) / square_size < 2:
            # for i in range(2 * (square_size), 3 * (square_size)):
            #     for j in range(1 * (square_size), 2 * (square_size)):
            #         square_nums.append(sud[i][j])
            # return square_nums
            return 7
        else:
            # for i in range(2 * (square_size), 3 * (square_size)):
            #     for j in range(2 * (square_size), 3 * (square_size)):
            #         square_nums.append(sud[i][j])
            # return square_nums
            return 9


# l.append(sud[i][0:(count % full_size) + 1])
def getSquareList(sud, row, square_size, sq, count):
    l = []
    full_size = square_size ** 2
    if sq == 0:
        # how many filled rows is the same as the current count (ex. 10) / 9 = 1
        filled_rows = int(count / full_size)
        for i in range(filled_rows):  # add already-full rows to the list
            l.append(sud[i*1][0:3])
        # for not-yet filled rows, go value by value. Final row is # of whatever's left of count after previous rows are taken care of.
        last_row = count - (filled_rows * full_size)
        l.append(sud[filled_rows][0:last_row])

    elif sq == 1:
        # how many filled rows is the same as the current count (ex. 10) / 9 = 1
        filled_rows = int(count / full_size)
        for i in range(filled_rows):  # add already-full rows to the list
            l.append(sud[i*1][3:6])
        # for not-yet filled rows, go value by value. Final row is # of whatever's left of count after previous rows are taken care of.
        last_row = count - (filled_rows * full_size)
        l.append(sud[filled_rows][3:last_row])

    elif sq == 2:
        # how many filled rows is the same as the current count (ex. 10) / 9 = 1
        filled_rows = int(count / full_size)
        for i in range(filled_rows):  # add already-full rows to the list
            l.append(sud[i*1][6:8])
        # for not-yet filled rows, go value by value. Final row is # of whatever's left of count after previous rows are taken care of.
        last_row = count - (filled_rows * full_size)
        l.append(sud[filled_rows][6:last_row])

    elif sq == 3:
        # how many filled rows is the same as the current count (ex. 10) / 9 = 1
        filled_rows = int(count / full_size)
        for i in range(int(filled_rows / 3)):  # add already-full rows to the list
            l.append(sud[i+3][0:3])
        # for not-yet filled rows, go value by value. Final row is # of whatever's left of count after previous rows are taken care of.
        last_row = count - (filled_rows * full_size)
        l.append(sud[filled_rows][0:last_row])

    elif sq == 4:
        # how many filled rows is the same as the current count (ex. 10) / 9 = 1
        filled_rows = int(count / full_size)
        for i in range(int(filled_rows / 3)):  # add already-full rows to the list
            l.append(sud[i+3][3:6])
        # for not-yet filled rows, go value by value. Final row is # of whatever's left of count after previous rows are taken care of.
        last_row = count - (filled_rows * full_size)
        l.append(sud[filled_rows][3:last_row])

    elif sq == 5:
        # how many filled rows is the same as the current count (ex. 10) / 9 = 1
        filled_rows = int(count / full_size)
        for i in range(int(filled_rows / 3)):  # add already-full rows to the list
            l.append(sud[i+3][6:8])
        # for not-yet filled rows, go value by value. Final row is # of whatever's left of count after previous rows are taken care of.
        last_row = count - (filled_rows * full_size)
        l.append(sud[filled_rows][6:last_row])

    elif sq == 6:
        # how many filled rows is the same as the current count (ex. 10) / 9 = 1
        filled_rows = int(count / full_size)
        for i in range(int(filled_rows / 6)):  # add already-full rows to the list
            l.append(sud[i+6][0:3])
        # for not-yet filled rows, go value by value. Final row is # of whatever's left of count after previous rows are taken care of.
        last_row = count - (filled_rows * full_size)
        l.append(sud[filled_rows][0:last_row])

    elif sq == 4:
        # how many filled rows is the same as the current count (ex. 10) / 9 = 1
        filled_rows = int(count / full_size)
        for i in range(int(filled_rows / 6)):  # add already-full rows to the list
            l.append(sud[i+6][3:6])
        # for not-yet filled rows, go value by value. Final row is # of whatever's left of count after previous rows are taken care of.
        last_row = count - (filled_rows * full_size)
        l.append(sud[filled_rows][3:last_row])

    elif sq == 5:
        # how many filled rows is the same as the current count (ex. 10) / 9 = 1
        filled_rows = int(count / full_size)
        for i in range(int(filled_rows / 6)):  # add already-full rows to the list
            l.append(sud[i+6][6:8])
        # for not-yet filled rows, go value by value. Final row is # of whatever's left of count after previous rows are taken care of.
        last_row = count - (filled_rows * full_size)
        l.append(sud[filled_rows][6:last_row])

    # return list(np.ravel(np.array(l)))
    # print(list(chain.from_iterable(l)))
    return list(chain.from_iterable(l))


main.counter = 0
main()
# print("tries: " + str(main.counter))

# def whatBox(row, col):
#     if row <= 2:
#         if col <= 2:
#             box = 1
#         elif col >= 3 and col <= 6:
#             box = 2
#         else:
#             box = 3
#     elif row >= 3 and row <= 6:
#         if col <= 2:
#             box = 4
#         elif col >= 3 and col <= 6:
#             box = 5
#         else:
#             box = 6
#     else:
#         if col <= 2:
#             box = 7
#         elif col >= 3 and col <= 6:
#             box = 8
#         else:
#             box = 9
#     return box
