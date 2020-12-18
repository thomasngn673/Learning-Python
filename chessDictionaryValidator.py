def isValidChessBoard(board):
    # Judge chess board based on number in piece position
    errors = 0
    for numKey in range(len(list(board.keys()))):
        # makes tuple board keys
        # converts tuple into list
        # finds the length of the list
        # creates the range from 0 to the end
        if int(list(board.keys())[numKey][0]) > 8 or int(list(board.keys())[numKey][0]) < 0:
            print('The given chess board is improper due to an error in numerical piece position.')
            errors = errors + 1

    # Judge chess board based on letter in piece position
    for letKey in range(len(list(board.keys()))):
        # makes tuple board keys
        # converts tuple into list
        # finds the length of the list
        # creates the range from 0 to the end
        if str(list(board.keys())[letKey][1]) not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
            print('The given chess board is improper due to an error in alphabetical piece position.')
            errors = errors + 1

    # Judge chess board based on if piece is black or white
    for pcolor in range(len(list(board.values()))):
        if str(list(board.values())[pcolor][0]) not in ['b', 'w']:
            print('The given chess board is improper due to an error in piece color.')
            errors = errors + 1

    # Judge chess board based on piece type
    for ptype in range(len(list(board.values()))):
        if str(list(board.values())[ptype][1:len(list(board.values())[ptype])]) not in ['pawn', 'knight', 'bishop',
                                                                               'rook', 'queen', 'king']:
            print('The given chess board is improper due to an error in piece type.')
            errors = errors + 1

    if errors > 0:
        print('There are ' + str(errors) + ' different type(s) of errors.')
    if errors == 0:
        print('The chess board has no errors.')


chessBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'bking'}
isValidChessBoard(chessBoard)