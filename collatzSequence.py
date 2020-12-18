import sys


def collatz(number):
    if number % 2 == 0:
        # % means divide and give remainder, if remainder is 0 the number is even
        return number // 2
        # return function is used instead of print functions
        # if 'print' function is used instead of 'return', assigning a global variable
        # later using the def collatz() will give a "None" data type rather than an 'int'
    else:
        return (3 * number) + 1


# print('Please input a number.')
# a = int(input())
#
# while True:
#     while collatz(a) != 1:
#         a = collatz(a)
#         print(a)
#     if collatz(a) == 1:
#         print(collatz(a))
#         sys.exit()

try:
    n = int(input('Please enter a number.'))
except ValueError:
    print('ValueError: please input an integer.')

while n != 1:
    n = collatz(n)
    print(n)
