allGuests = {'Alice': {'apples': 4, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}


def totalBrought(guestlist, item):
    numBrought = 0
    for val in guestlist.values():  # loops through all values in key-value pairs
        numBrought = numBrought + val.get(item, 0)  # "gets" specified item, if not present default to 0
    return numBrought


print('Number of Items Brought')
print('-----------------------')
print('- Apples: ' + str(totalBrought(allGuests, 'apples')))
print('- Pretzels: ' + str(totalBrought(allGuests, 'pretzels')))
print('- Ham Sandwiches: ' + str(totalBrought(allGuests, 'ham sandwiches')))
print('- Cakes: ' + str(totalBrought(allGuests, 'cakes')))
print('- Cups: ' + str(totalBrought(allGuests, 'cups')))
print('- Apple Pies: ' + str(totalBrought(allGuests, 'apple pies')))