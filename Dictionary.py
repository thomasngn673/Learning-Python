groceries = {'bananas': 5, 'oranges': 3}
# 'bananas':5 is called a key-value pair

print(groceries['bananas'])
# gives value 5
print(groceries.get('oranges'))
# same function as above, gets value associated with key

contacts = {
    'Thomas': ['988-8563', 'thomasngn673@gmail.com'],
    'Ashley': ['844-7729', 'ashleypham3801@gmail.com']
}

print(contacts.get('Thomas'))

contacts2 = {
    'Bob': {'phone': '123-4567', 'email': 'bob@gmail.com'},
    'George': {'phone': '987-6543', 'email': 'george@gmail.com'}
}
print((contacts2.get('Bob')).get('phone'))


word_counts = {
    'I': 1,
    'like': 1,
    'pizza': 3
}

# dict.items()
# generates a list of tuples which is a key-value pair
print(word_counts.items())

# dict.keys()
print(word_counts.keys())
# dict.values()
print(word_counts.values())
# generates list of only values

word_counts.pop('I')
# gives tuple key-value pair of the specified entry
print(word_counts)
# deletes tuple from list

word_counts.popitem()
# gives tuple key-value pair of the last entry
print(word_counts)
# deletes tuple from list

word_counts['Aaron'] = 2
# add Aaron to end of dictionary

word_counts.clear()
# clear dictionary

sorted(list(word_counts.values()))
# gives list of values in numerical order

