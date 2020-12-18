# Conway's Game of Life Rules
# 1. If a living square has 2-3 living neighbors, it continues to live
# 2. If a dead square has exactly 3 living neighbors, it comes to live
import random, time, copy


width = 12
height = 4

# creates a list of x values that each have own individual list of y values
# creates a list of lists
nextCells = []
for x in range(width):
    column = []  # create a new column
    for y in range(height):
        if random.randint(0, 1) == 0:
            column.append('#')  # add a living cell
        else:
            column.append(' ')  # add a dead cell
    nextCells.append(column)

while True:  # main program loop
    print('\n\n\n\n\n')  # separate each step with newlines
    currentCells = copy.deepcopy(nextCells)

    # print currentCells on the screen
    for y in range(height):
        for x in range(width):
            print(currentCells[x][y], end='')  # prints the '#' or 'space'
            # "for y in range" is put first because "end=''" deletes newline
            # "end=''" creates horizontal prints, so order is reversed
            # in current loop, y value does not change, only x
        print()  # prints a newline at the end of the row
        # without this, the entire box is printed on one line

    # calculate the next step's cells based on current step's cells
    for x in range(width):
        for y in range(height):
            # % ensures that the number is always positive, doesn't change value of (x-1) unless negative
            leftCoord = (x-1) % width
            rightCoord = (x+1) % width
            aboveCoord = (y-1) % height
            belowCoord = (y+1) % height

            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1  # top-left neighbor is alive
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1  # top neighbor is alive
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1  # top-right neighbor is alive
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1  # left neighbor is alive
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1  # right neighbor is alive
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1  # bottom-left neighbor is alive
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1  # bottom neighbor is alive
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1  # bottom-right neighbor is alive

            # set cell based on the rules
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                # living cells with 2 or 3 neighbors stay alive
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # dead cells with 3 neighbors become alive
                nextCells[x][y] = '#'
            else:
                nextCells[x][y] = ' '
    time.sleep(1)