import random, sys
# import sys allows sys.exit() which breaks out entire system instead of multiple breaks
print('ROCK, PAPER, SCISSORS')
wins = 0
losses = 0
ties = 0

while True:
    print('Wins: ' + str(wins) + ', ' + 'Losses: ' + str(losses) + ', ' + 'Ties: ' + str(ties))
    print()
    print('Enter your move: (r)ock, (p)aper), (s)cissors, (q)uit.')
    your_move = input()
    if your_move == 'q':
        sys.exit()
    if your_move == 'r' or your_move == 'p' or your_move == 's':
        if your_move == 'r':
            print('Your move: ROCK')
        if your_move == 'p':
            print('Your move: PAPER')
        if your_move == 's':
                print('Your move: SCISSORS')

        com_num = random.randint(1, 3)
        if com_num == 1:
            com_move = 'r'
            print('Computer move: ROCK')
        if com_num == 2:
            com_move = 'p'
            print('Computer move: PAPER')
        if com_num == 3:
            com_move = 's'
            print('Computer move: SCISSORS')

        if your_move == com_move:
            ties = ties + 1

        if your_move == 'r' and com_move == 'p':
            losses = losses + 1
        if your_move == 'r' and com_move == 's':
            wins = wins + 1

        if your_move == 'p' and com_move == 's':
            losses = losses + 1
        if your_move == 'p' and com_move == 'r':
            wins = wins + 1

        if your_move == 's' and com_move == 'r':
            losses = losses + 1
        if your_move == 's' and com_move == 'p':
            wins = wins + 1
