import random


def main():
    size = 9
    square_size = int(size / 3)
    num_list = list(range(1, size + 1))
    # init
    sudoku = []
    for i in range(size):
        line = []
        sudoku.append(line)

    # create sudoku!
    print('creating...')
    # sudoku[0][0] = random.randint(1, size)
    for i in range(size):
        while len(sudoku[i]) < size:
            # num = random.randint(1, size)
            try:
                # get random number from possible random numbers not yet tried
                num = random.choice(num_list)
            except IndexError:
                # if all numbers have been tried, a number can't be taken from an empty list. Error and exit.
                print('Generation error: ran out of numbers to choose from')
                exit()
            # refresh match
            match = False

            print('i: ' + str(i))
            print("num: " + str(num))
            PrintSudoku(sudoku, size)

            # not the same row
            for j in range(len(sudoku[i])):
                if num == sudoku[i][j]:
                    print('same row')
                    match = True

            # if not the same row until now
            if not match:
                # not the same column
                for j in range(i):
                    # print('j: ' + str(j) +
                    #   '\tlen(sudoku[i]): ' + str(len(sudoku[i])))
                    if num == sudoku[j][len(sudoku[i])]:
                        print('same col')
                        match = True

            # if not same row nor column
            if not match:
                # not the same square
                square = getSquare(sudoku, i, square_size)
                print('square: ' + str(square))
                # square_list = getSquareList(sudoku, i, square_size, square)

            if not match:
                # add to sudoku
                sudoku[i].append(num)
                # refresh the random number list, for next number to choose again
                num_list = list(range(1, size + 1))
                print()
            else:
                # remove the random number from the list, to not choose again.
                num_list.remove(num)

    PrintSudoku(sudoku, size)


def PrintSudoku(sud, size):
    for i in range(size):
        print(sud[i])


def getSquare(sud, row, square_size):
    square_nums = []
    print(len(sud[row]))
    if len(sud[row]) > 0 and row > 0:
        if row / square_size < 1:
            if (len(sud[row])) / square_size < 1:
                for i in range(0 * (square_size), 1 * (square_size)):
                    for j in range(0 * (square_size), 1 * (square_size)):
                        square_nums.append(sud[i][j])
                return square_nums
                # return 1
            elif (len(sud[row])) / square_size >= 1 and (len(sud[row])) / square_size < 2:
                for i in range(0 * (square_size), 1 * (square_size)):
                    for j in range(1 * (square_size), 2 * (square_size)):
                        square_nums.append(sud[i][j])
                return square_nums
                # return 2
            else:
                for i in range(0 * (square_size), 1 * (square_size)):
                    for j in range(2 * (square_size), 3 * (square_size)):
                        square_nums.append(sud[i][j])
                return square_nums
                # return 3
        elif row / square_size >= 1 and row / square_size < 2:
            if (len(sud[row])) / square_size < 1:
                for i in range(1 * (square_size), 2 * (square_size)):
                    for j in range(0 * (square_size), 1 * (square_size)):
                        square_nums.append(sud[i][j])
                return square_nums
                # return 4
            elif (len(sud[row])) / square_size >= 1 and (len(sud[row])) / square_size < 2:
                for i in range(1 * (square_size), 2 * (square_size)):
                    for j in range(1 * (square_size), 2 * (square_size)):
                        square_nums.append(sud[i][j])
                return square_nums
                # return 5
            else:
                for i in range(1 * (square_size), 2 * (square_size)):
                    for j in range(2 * (square_size), 3 * (square_size)):
                        square_nums.append(sud[i][j])
                return square_nums
                # return 6
        else:
            if (len(sud[row])) / square_size < 1:
                for i in range(2 * (square_size), 3 * (square_size)):
                    for j in range(0 * (square_size), 1 * (square_size)):
                        square_nums.append(sud[i][j])
                return square_nums
                # return 7
            elif (len(sud[row])) / square_size >= 1 and (len(sud[row])) / square_size < 2:
                for i in range(2 * (square_size), 3 * (square_size)):
                    for j in range(1 * (square_size), 2 * (square_size)):
                        square_nums.append(sud[i][j])
                return square_nums
                # return 8
            else:
                for i in range(2 * (square_size), 3 * (square_size)):
                    for j in range(2 * (square_size), 3 * (square_size)):
                        square_nums.append(sud[i][j])
                return square_nums
                # return 9


def getSquareList(sud, row, square_size, sq):
    # l = []
    # if len(sud[row]) > 0:
    #     for i in range(len(sud[row])):
    return l


main()

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
