def comma(list):
    for index in range(len(list)-1):
        print(list[index] + ', ', end='')
    print('and ' + (list[len(list)-1]))

spam = ['apples', 'bananas', 'tofu', 'cats', 'dogs', 'cups', 'mouse', 'keyboard']
comma(spam)