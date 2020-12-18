import random


# create a coin flip 100 times find probability of flipping a 6 streak, redo 10000 times
numberOfStreaks = 0
Streaks = 0
CoinFlip = []
for experimentNumber in range(10000):  # set experiment to run 10,000 times
    for flips in range(100):  # set flips in one experiment to 100 flips
        CoinFlip.append((random.randint(0, 1)))  # add to CoinFlip list 'heads' or 'tails'
        if flips == 0:  # if index is equal to 0, ignore because CoinFlip[0-1] isn't valid
            pass
        elif CoinFlip[flips] == CoinFlip[flips-1]:  # if value of flip is equal to the last flip, add streak
            Streaks += 1
        else:
            Streaks = 0  # reset Streaks if there is a change in flip value (heads to tails, tails to heads)
        if Streaks == 6:  # if streak adds up to 6, add 1 to numberOfStreaks
            numberOfStreaks += 1
    CoinFlip = []  # reset CoinFlip list for next experiment (numberOfStreaks is still kept)

print('Chance of streak: %s%%' % (numberOfStreaks / (100*10000)))