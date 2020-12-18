import random


width = 9
height = 6

cells = []  # creates list made up of ...
for x in range(width):
    column = []
    # ... these lists
    for y in range(height):
        if random.randint(0, 1) == 0:
            column.append('O')
        else:
            column.append('.')
    cells.append(column)

for y in range(height):
    for x in range(width):
        print(cells[x][y], end='')
    print()
