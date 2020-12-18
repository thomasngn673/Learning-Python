import turtle

thomas_turtle = turtle.Turtle()


def square():
    thomas_turtle.forward(100)
    thomas_turtle.right(90)
    thomas_turtle.forward(100)
    thomas_turtle.right(90)
    thomas_turtle.forward(100)
    thomas_turtle.right(90)
    thomas_turtle.forward(100)


square()
thomas_turtle.forward(200)
square()

# only 'import turtle' & 'turtle.movement(a)' are needed to run function
# turtle.movement is redefined in thomas_turtle which then creates the new need to call this variable

elephant_weight = 3000
ant_weight = 0.1

if elephant_weight > ant_weight:
    square()
else:
    thomas_turtle.forward(100)

thomas = 'happy'
while thomas == 'happy':
    thomas_turtle.forward(10)

for count in range(4):
    square()

digits = [0, 1, 2, 3, 4, 5]
len(digits)
# len is length function
print(digits[0:5])
# 0:5 index from i:0 to i:5
print(digits[0:-1])
# 0:-1 index from i:0 to i:4
print(digits[0:5:1])
# 0:5:1 index from i:0 to i:5 in increments of 1
print(digits[::])
# entire array

# list casting is list()
names = ["Thomas", "Ashley"]
names.append("Ella")
print(names)
# append adds an element to the end of the array
names.insert(0, "Ella")
# insert adds inserts element at specified index
names.remove("Thomas")
# remove takes out specified string
names.reverse()
# reverses the order of the entire array
names.sort()
# sorts the array in numerical order

adj = 'hungry, tall, short, pretty'
a = adj.split(", ")
# splits the characters between each word, into 4 different parts
b = ' and '.join(a)
# 'string'.join(array) joins the components of an array with the 'string'

# tuple casting is tuple()
# tuple is a list with parentheses and constraints
# you can't add/change elements to it (append, insert, etc.)
daughter = ("Ella", 8,"brownies")
son = ("Aiden", 5, "pizza")
children = [daughter, son]
# name, age, favFood = daughter
# print(name)
# print(age)
# print(favFood)
for name, age, favFood in children:
    print(name)
    print(age)
    print(favFood)
    print()

# set casting is set()
# sets is a list that uses {}, gives random order synonymous to a bag
fruit = {'blueberry', 'raspberry'}
fruit.add('strawberry')
# add string to the list
# if string is a duplicate, it is not added to list set unlike an array
l = [1, 2, 2, 3, 3, 3, 4, 4, 5]
no_duplicates = set(l)
shelf1 = {'Harry Potter', 'Percy Jackson'}
shelf2 = {'Harry Potter', 'Hunger Games'}
library = shelf1.union(shelf2)
# combines both sets ignoring duplicates
both_shelves = shelf1.intersection(shelf2)
# shows what strings are in common between both sets
available_books = shelf1.difference(shelf2)
# gives the books in shelf1 that are not in shelf2
