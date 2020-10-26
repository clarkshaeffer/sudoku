import sudoku_obj
import sudoku_lib
# from lib import sudoku_obj
# from lib import sudoku_lib
import random
# print('''
#       ___         ___        _____        ___         ___         ___
#      /  /\       /__/\      /  /::\      /  /\       /__/|       /__/\
#     /  /:/_      \  \:\    /  /:/\:\    /  /::\     |  |:|       \  \:\
#    /  /:/ /\      \  \:\  /  /:/  \:\  /  /:/\:\    |  |:|        \  \:\
#   /  /:/ /::\ ___  \  \:\/__/:/ \__\:|/  /:/  \:\ __|  |:|    ___  \  \:\
#  /__/:/ /:/\:/__/\  \__\:\  \:\ /  /:/__/:/ \__\:/__/\_|:|___/__/\  \__\:\
#  \  \:\/:/~/:\  \:\ /  /:/\  \:\  /:/\  \:\ /  /:\  \:\/:::::\  \:\ /  /:/
#   \  \::/ /:/ \  \:\  /:/  \  \:\/:/  \  \:\  /:/ \  \::/~~~~ \  \:\  /:/
#    \__\/ /:/   \  \:\/:/    \  \::/    \  \:\/:/   \  \:\      \  \:\/:/
#      /__/:/     \  \::/      \__\/      \  \::/     \  \:\      \  \::/
#      \__\/       \__\/                   \__\/       \__\/       \__\/
# ''')

difficulty_prompt = '''

Choose your difficulty! (input the number below)

1. Baby's First Sudoku 40 hidden
2. Very Easy 45 hidden
3. Easy 49
4. Medium 53
5. Challenging 56
6. Hard 59
7. Very Hard 61
8. Dark Souls of Sudokus 64
'''

print(difficulty_prompt)

errors = -1  # no user value errors yet
inp = '0'
while int(inp) < 1 or int(inp) > 8:  # while the string-cast-int is not in range, get input
    errors += 1  # user error
    if errors >= 5:  # if 5 user errors or more, print prompt again
        print(difficulty_prompt)
    try:  # don't freak out if it isn't an int
        inp = int(input('> '))  # receive input
    except ValueError:
        pass


hidden = 0
if inp == 1:
    hidden = 40
elif inp == 2:
    hidden = 45
elif inp == 3:
    hidden = 49
elif inp == 4:
    hidden = 53
elif inp == 5:
    hidden = 56
elif inp == 6:
    hidden = 59
elif inp == 7:
    hidden = 61
elif inp == 8:
    hidden = 64

shown = 81 - hidden

original_sudoku = sudoku_obj.Sudoku()
puzzle = original_sudoku

hidden_count = 0
for i in range(81):
    if hidden_count < hidden:
        if random.randint(1, 81) <= hidden:
            puzzle.sudoku[i] = 0
            hidden_count += 1
    else:
        i = 81

sudoku_lib.PrintSudoku(puzzle.sudoku)

while inp != 'ready':
    inp = input(
        "Write this on a piece of paper, and go ham!\nWhen ready to check the answer, type 'ready'.\n> ")


sudoku_lib.PrintSudoku(original_sudoku.sudoku)
