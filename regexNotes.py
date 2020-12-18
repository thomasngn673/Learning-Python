import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # assigns Regex object to phoneNumRegex
# r before \d creates a raw string, which prints all the text following it regardless of char type
mo = phoneNumRegex.search('My number is 415-555-4242.')  # searches (message) for phoneNumRegex
# creates a "match" object
print('Phone number found: ' + mo.group())

# REGEX GROUPING
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
mo.group(1)  # prints '415'
mo.group(2)  # prints '555-4242'
mo.group(0)  # prints entire phone number
mo.group()  # prints entire phone number

areaCode, mainNumber = mo.groups()  # prints tuple list with all objects ('415','555-4242')
print(areaCode)
print(mainNumber)

# REGEX GROUPING WITH PARENTHESES IN STRING
phoneNumRegex = re.compile(r'(\( \d\d\d \))-(\d\d\d-\d\d\d\d)')
# \( and \) are escape characters, and match only because it is a raw string
# it will have a different function in a normal string
mo = phoneNumRegex.search('My number is (415)-555-4242.')
mo.group(1)
mo.group(2)

# REGEX GROUPING WITH THE PIPE ('OR' COMMAND)
heroRegex = re.compile(r'Batman|Superman')  # will match either Batman or Superman
mo1 = heroRegex.search('Batman and Superman')  # matches the first hero that appears
mo1.group()
mo2 = heroRegex.search('Superman and Batman')  # matches the first hero that appears
mo2.group()

# REGEX GROUPING WITH SAME PREFIX
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')  # matches and groups all possible objects with prefix 'Bat'
mo = batRegex.search('The Batmobile lost a wheel.')
mo.group()
mo.group(1)

# REGEX GROUPING WITH QUESTION MARK - OPTIONAL MATCHING
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')  # since (wo) isn't in the string, Batman is matched by default
mo1.group()

mo2 = batmanRegex.search('The Adventures of Batwoman')
mo2.group()

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242.')
mo1.group()
mo2 = phoneRegex.search('My number is 555-4242.')
mo2.group()

# REGEX GROUPING WITH ASTERISK - MATCH ZERO OR MORE
batRegex = re.compile(r'Bat(wo)*man')

mo1 = batRegex.search('The Adventures of Batman')  # (wo) matches 0 times
mo1.group()

mo2 = batRegex.search('The Adventures of Batwoman')  # (wo) matches 1 time
mo2.group()

mo3 = batRegex.search('The Adventures of Batwowowowowowoman')  # (wo) matches 6 times
mo3.group()

# REGEX GROUPING WITH PLUS - MATCH ONE OR MORE
batRegex = re.compile(r'Bat(wo)+man')

mo1 = batRegex.search('The Adventures of Batwoman')  # (wo) matches 1 time
mo1.group()

mo2 = batRegex.search('The Adventures of Batwowowowoman')  # (wo) matches 4 time
mo2.group()

mo3 = batRegex.search('The Adventures of Batman')  # mo3 reads as None because it doesn't appear in the string

# REGEX GROUPING WITH BRACES
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
mo1.group()

mo2 = haRegex.search('Ha')  # mo2 reads as None because it doesn't appear 3 times in the string

# GREEDY AND NONGREEDY MATCHING
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
mo1.group()  # matches MAXIMUM available (5)

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
mo2.group()  # matches MINIMUM available (3)

# FINDALL
# normal .search function only finds first appearance from compile
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumRegex.findall('Cell: 415-555-9999, Work: 212-555-0000')

# if there are parentheses, the findall function returns tuples
phoneNumRegex = re.compile(r'\(\d\d\d-\d\d\d-\d\d\d\d\)')
phoneNumRegex.findall('Cell: 415-555-9999, Work: 212-555-0000')

# CHARACTER CLASSES
# \d - any number from 0 to 9
# \D - any non-digit number from 0 to 9
# \w - any letter, number, underscore
# \W - any non-letter, non-number, non-underscore
# \s - any space, tab, newline
# \S - any non-space, non-tab, non-newline
xmasRegex = re.compile(r'\d+\s\w+')
xmasRegex.findall('12 dummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, '
                  '2 doves, 1 partridge')

# CUSTOM CHARACTER CLASSES
vowelRegex = re.compile(r'[aeiouAEIOU]')  # will match any vowel, lowercase or uppercase
vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
# when using escape characters in re.compile[ ], \ is not needed
consonantRegex = re.compile(r'[^aeiouAEIOU]')  # ^ is negative char class, matches everything not in the brackets
consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')  # matches consonants, punctuation, spaces

# CARET AND DOLLAR SIGN CHARACTERS - BEGINNING AND ENDING STRING MATCHING
beginsWithHello = re.compile(r'^Hello')  # match must occur at the beginning of searched text
beginsWithHello.search('Hello, world!')

endsWithNumber = re.compile(r'\d$')  # match must occur at the end of the searched text
endsWithNumber.search('Your number is 42')

wholeStringIsNum = re.compile(r'^\d+$')  # must start and end with at least one digit
wholeStringIsNum.search('12345678')
# CARROTS costs DOLLARS - to remember order of carets & dollar signs

# DOT - MATCH SINGLE CHARACTER BUT NEWLINE
atRegex = re.compile(r'.at')
atRegex.findall('The cat in the hat sat on the flat mat.')
# 'flat' is matched as 'lat' because .compile function only matched 1 character

# DOT-STAR - MATCH ALL BUT NEWLINE
nameRegex = re.compile(r'First Name: (.*), Last Name: (.*)')
mo = nameRegex.search('First Name: Al, Last Name: Nguyen')
mo.group(1)
mo.group(2)

# "Match an opening angle bracket, followed by anything, followed by a closing angle bracket"
# optional match for opening bracket, .* matches everything after
# nongreedy Regex
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
mo.group()

# greedy Regex
greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
mo.group()

# DOT - MATCHING NEWLINES
noNewlineRegex = re.compile(r'.*')
noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
# only prints 'Serve the public trust.' dot character matches until newline

newlineRegex = re.compile('.*', re.DOTALL)
newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
# re.DOTALL applies dot to all, including \n characters

# REVIEW OF REGEX SYMBOLS
# ? matches zero or one
# * matches zero or more
# + matches one or more
# {n} matches exactly n
# {n,} matches n or more
# {,m} matches 0 to m
# {n,m} matches n to m
# {n,m}? or *? or +? is nongreedy match
# ^spam says string must begin with spam
# spam$ says string must end with spam
# . matches one character but newline
# .* matches all but newline
#       re.DOTALL applies dot to entire message (even if it contains newline)
# \d, \s, \w matches any digit, space, word
# \D, \S, \W matches any but digits, spaces, words
# [abc] matches everything in brackets
#       '-' can be used to make a range
# [^abc] matches any character not in the bracket

# CASE-INSENSITIVE MATCHING
robocop = re.compile(r'robocop', re.I)
robocop.search('RoboCop is part man, part machine, all cop.').group()
# matches to whatever robocop is found in the string
# in this case, it is 'RoboCop'

# STRING SUBSTITUTION
namesRegex = re.compile(r'Agent \w+')  # matches with each letter in 'Alice' until the space
namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
# matches with 'Agent Alice', then replaces with 'CENSORED'

agentNamesRegex = re.compile(r'Agent(\w)\w*')  # match 'Agent (first letter) (remaining word)' and ...
agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
# ... replaces with \1****, \1 references to group 1 which is the first letter of the name

# VERBOSE - IGNORE COMMENT, WHITESPACE, NEWLINES TO MAKE .COMPILE() EASIER TO READ
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?  # area code
(\s|-|\.)?  # separator
\d{3}  # first 3 digits
(\s|-|\.)  # separator
\d{4}  # last 4 digits 
(\s*(ext|x|ext.) \s* d{2,5})?  # extension 
)''', re.VERBOSE)
