def displayInventory(inventory):
    print('Inventory')
    print('---------')
    totalItems = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + str(k))
        totalItems = totalItems + v
    print('Total number of items: ' + str(totalItems))


stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
displayInventory(stuff)