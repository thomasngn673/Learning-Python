# DOUBLE QUOTES
print("That is Ashley's Airpods.")

# ESCAPE CHARACTERS
print()
print('Say hi to Bob\'s mother.')
# \'   \"   \t   \n   \\

# RAW STRINGS
print()
print(r'That is Carol\'s cat.')
# everything in a raw string is counted as part of the string

# MULTILINE, works with triple single quotes and triple double quotes
print()
print('''Dear Alice,

SMD

Sincerely,
Thomas''')

# STRING INTERPOLATION WITH %S
print()
name = 'Al'
age = 4000
print('My name is %s. I am %s years old.' % (name, age))

# F-STRINGS
print()
print(f'My name is {name}. I am {age + 1} years old.')

# CONVERT STRING TO UPPER/LOWER CASE
print()
spam = 'Hello, World!'
print(spam.upper())
print(spam.lower())
# spam.islower, spam.isupper checks if the string is lower/upper case

# isX() METHODS
# isalpha() checks if string is only letters
# isalnum() checks if string is only letters and numbers
# isdecimal() checks if string is only numbers
# isspace() checks if string is only spaces, tabs, newlines
# istitle() checks if string is made of words that start with upper case followed by lower case only

print()
while True:
    print('Select a new password (letters and numbers only).')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')

# CHECK START AND END
'Hello, world!'.startswith('Hello')
'Hello, world!'.endswith('world!')

# JOIN STRINGS
', '.join(['cats', 'rats', 'bats'])
# 'thing joining list'.join([list])

# SPLIT STRINGS
# splits strings into sections using string in parentheses and deletes it
'My name is Simon'.split()
# 'string'.split(), string is split where there are spaces
'MyABCnameABCisABCSimon'.split('ABC')

# PARTITION STRINGS
# splits original string into smaller strings before and after the string in the parentheses
'Hello, world!'.partition('w')
before, sep, after = 'Hello, world!'.partition(' ')
# can assign partitioned string to variables

# RIGHT, LEFT, CENTER ADJUST
# adjust by spaces in parentheses
'Hello'.rjust(10, '-')

# REMOVING WHITESPACE
spam = '     Hello, World     '
spam.strip()
# removes the white spaces
spam.lstrip()
# removes white space on the left side
spam.rstrip()
# removes white space on the right side
spam = 'SpamSpamBaconSpamEggsSpamSpam'
spam.strip('ampS')
# removes "Spam" before and after
# order of the characters doesn't matter

# PYPERCLIP MODULE
import pyperclip
pyperclip.copy('Hello, world!')
pyperclip.paste()



