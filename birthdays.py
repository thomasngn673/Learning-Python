import sys


birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True:
    name = input('Enter name or a blank to quit (case-sensitive). \n')
    if name == '':
        sys.exit()
    if name in birthdays:  # check if input is in dictionary
        print('The birthday of ' + name + ' is ' + birthdays[name] + '.')
        print()
    else:
        birthdate = input('I do not information for ' + name + '. When is their birthday? \n')
        birthdays[name] = birthdate  # add new entry to dictionary dictionary[key] = value
        print('Database has been updated.')
        print()

# dictionaries can only be searched using their keys, not values

spam = {}
spam['1'] = 'mouse'
spam['2'] = 'cup'
spam['3'] = 'love'
print(spam)
print(list(spam))
# converted a dictionary/tuple into a list deletes the value in the key-value pair
# only the the key is displayed

# tuple.values(), tuple.keys(), tuple.items()
