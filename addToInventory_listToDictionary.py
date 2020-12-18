def addToInventory(inventory, addedItems):
    print('Inventory')
    print('---------')
    addedItemsDict = {}
    totalItems = 0

    # convert addedItems data type list to addedItems data type dictionary
    for thing in addedItems:  # loops through all objects in list
        addedItemsDict.setdefault(thing, 0)
        # add things from addedItems list to addedItems dictionary
        # ex. runs through 'gold coin', adds to addedItemsDict, assigns default value to 0
        addedItemsDict[thing] = addedItemsDict[thing] + 1
        # assigns value to key
        # every time "thing" appears, add 1
        # ex. 1st time running through 'addedItemsDict[thing] = 0 + 1'
        # 0 is from setdefault(thing, 0)

    # add objects from addedItems to inventory
    for thingy in addedItemsDict.keys():  # runs through all keys in addedItemsDict
        if thingy not in inventory:  # if there is a new item not in the original inventory ...
            inventory[thingy] = addedItemsDict[thingy]
            # ... add to original inventory
            # inventory[thingy] adds a new entry to original inventory, creates key in key-value pair
            # addedItemsDictionary[thingy] gives the value in key-value pair
            # ex. inventory[dagger] --> not in original inventory
            #     addedItemsDict[dagger] = 1
            #     inventory[dagger] = 1
            #     inventory = { ... , 'dagger': 1}
        else:  # if item is already present in original inventory ...
            inventory[thingy] = inventory[thingy] + addedItemsDict[thingy]
            # ... newValue = oldInventoryValue + addedItemsValue

    for k, v in inventory.items():  # loops through key-pair
        print(str(v) + ' ' + str(k))  # ex. 45 gold coins
        totalItems = totalItems + v  # add value to totalItems every loop

    print()
    print('Total number of items: ' + str(totalItems))


inv = {'gold coin': 42, 'rope': 1, 'mouse': 4}
dragonLootList = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'sapphire', 'sapphire']

addToInventory(inv, dragonLootList)