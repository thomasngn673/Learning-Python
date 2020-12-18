import random

# num = (random.randint(1, 20))
# print('I am thinking of a number between 1 and 20.')
# print('Take a guess.')
# loop_counter = 0
# while True:
#     your_guess = input()
#     loop_counter = loop_counter + 1
#     if int(your_guess) < num:
#         print('Your guess is too low.')
#         print('Take a guess.')
#     if int(your_guess) > num:
#         print('Your guess is too high.')
#         print('Take a guess.')
#     if int(your_guess) == num:
#         print('Good job! You guessed my number in ', str(loop_counter), ' guesses.')
#         break

num = random.randint(1, 20)
print('I am thinking of a number between 1 and 20. Take a guess.')
for num_guess in range(1, 7):
    guess = input()
    if int(guess) < num:
        print('Your guess was too low.')
        print('Take a guess.')
    elif int(guess) > num:
        # elif = else if statement,
        print('Your guess was too high.')
        print('Take a guess.')
    else:
        break

if int(guess) == num:
    print()
    print('Good job! You guessed my number in', str(num_guess), 'guesses.')
else:
    print()
    print('Nice try. The number I was thinking of was ' + str(num) + '.')