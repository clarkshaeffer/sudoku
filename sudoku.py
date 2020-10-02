import random

size = 9


def main():
    # init
    sudoku = []
    for i in range(size):
        line = []
        sudoku.append(line)

    # create sudoku!
    print('creating...')
    # sudoku[0][0] = random.randint(1, size)
    for i in range(size):
        print('i' + str(i))
        while len(sudoku[i]) < size:
            num = random.randint(1, size)
            print(str(sudoku[i]) + ' ' + str(num))
            match = False
            # not the same row
            for j in range(len(sudoku[i])):
                if num == sudoku[i][j]:
                    print('same row')
                    match = True

            # not the same column
            print(i)
            for j in range(i):
                if num == sudoku[j][len(sudoku[i]) - 1]:
                    print('same col')
                    match = True
            if not match:
                sudoku[i].append(num)

    # while len(sudoku[0]) < size:
    # #   num = random.randint(1, size)
    #     match = False
    #     for j in range(len(sudoku[0])):
    #         if num == sudoku[0][j]:
    #             match = True
    #     if  not match:
    #         sudoku[0].append(num)
#
    # # secon  line
    # while len(sudoku[1]) < size:
    # #   num = random.randint(1, size)
    #     match = False
    #     # not the same row
    #     for j in range(len(sudoku[1])):
    #         if num == sudoku[1][j]:
    #             match = True
    #     # n t the same column
    #     if num  = sudoku[0][len(sudoku[1])]:
    #         match = True
    #     if not match:
    #         sudoku[1].append(num)
 #
    # x amount of lines
    PrintSudoku(sudoku, size)


def whatBox(row, col):
    if row <= 2:
        if col <= 2:
            box = 1
        elif col >= 3 and col <= 6:
            box = 2
        else:
            box = 3
    elif row >= 3 and row <= 6:
        if col <= 2:
            box = 4
        elif col >= 3 and col <= 6:
            box = 5
        else:
            box = 6
    else:
        if col <= 2:
            box = 7
        elif col >= 3 and col <= 6:
            box = 8
        else:
            box = 9
    return box


def PrintSudoku(sud, size):
    for i in range(size):
        print(sud[i])


main()
