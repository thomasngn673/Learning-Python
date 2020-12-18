import pprint


message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:  # not in RANGE
    count.setdefault(character, 0)  # if character currently looped is not in message, set value = 0
    count[character] = count[character] + 1  # add character to 'count' dictionary, add 1 to character

pprint.pprint(count)  # "pretty print" displays entries in vertical order
print()
print(pprint.pformat(count))  # equivalent to pprint.pprint
