theBoard = {'top-left': ' ', 'top-mid': ' ', 'top-right': ' ', 'mid-left': ' ', 'mid-mid': ' ', 'mid-right': ' ',
            'low-left': ' ', 'low-mid': ' ', 'low-right': ' '}


def printBoard(board):
    print(board['top-left'] + '|' + board['top-mid'] + '|' + board['top-right'])
    print('-+-+-')
    print(board['mid-left'] + '|' + board['mid-mid'] + '|' + board['mid-right'])
    print('-+-+-')
    print(board['low-left'] + '|' + board['low-mid'] + '|' + board['low-right'])


for turn in range(9):
    printBoard(theBoard)  # print

    xspace = input('Player X move: what space? \n')
    while xspace not in theBoard:
        xspace = input('Please enter valid position. \n')
    while theBoard[xspace] == 'X' or theBoard[xspace] == 'O':
        xspace = input('This spot has already been filled. Please enter another position. \n')
        while xspace not in theBoard:
            xspace = input('Please enter valid position. \n')
    if theBoard[xspace] == ' ':
        theBoard[xspace] = 'X'

    printBoard(theBoard)

    ospace = input('Player O move: what space? \n')
    while ospace not in theBoard:
        ospace = input('Please enter valid position. \n')
    while theBoard[ospace] == 'X' or theBoard[ospace] == 'O':
        ospace = input('This spot has already been filled. Please enter another position. \n')
        while ospace not in theBoard:
            ospace = input('Please enter valid position. \n')
    if theBoard[ospace] == ' ':
        theBoard[ospace] = 'O'
