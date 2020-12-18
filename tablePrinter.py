def printTable(table):
    colWidths = [0] * len(table)  # creates a list of 0's with length of tableData
    # ex. colWidths = [0] * 3 --> [0, 0, 0]

    for y in range(len(table)):  # loops through the number of lists of lists
        for x in table[y]:  # loops through every string in the first list, second list, etc...

            # Finding the longest string within each list, assigns length of longest string to column[y]
            # if longest string is found, if statement is skipped
            if colWidths[y] < len(x):  # if the value of colWidths[y] is less than the length of the string at
                # tableData[y] ...
                colWidths[y] = len(x)  # ... assign the value to the value of length of string of x

    for x in range(len(table[0])):  # find number of rows [y]
        for y in range(len(table)):  # find number of columns [x]
            print(table[y][x].rjust(colWidths[y]), end=' ')  # replaces last character in line with space, deletes
            # default newline
            # table [y][x] because orientation of desired product is inverted compared to original table
        print()


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
