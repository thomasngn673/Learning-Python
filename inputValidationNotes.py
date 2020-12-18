import pyinputplus as pyip

# BASIC pyip.inputNum() PARAMETERS
response = pyip.inputNum()  # checks if input is a number
response = pyip.inputNum('Enter num: ', min=4)  # checks if input is at a minimum of 4
response = pyip.inputNum('Enter num: ', greaterThan=4)  # checks that input must be greater than 4
response = pyip.inputNum(blank=True)  # doesn't allow blank answers unless blank=True
response = pyip.inputNum(limit=2)  # allows 2 failed attempts before ending function and outputting "exception"
response = pyip.inputNum(timeout=10)  # allows 10 seconds of waiting before ending function and outputting "exception"
response = pyip.inputNum(limit=2, default=N/A)  # sets N/A instead of "exception" in case of failure

# ALLOWREGEXES AND BLOCKREGEXES
response = pyip.inputNum(allowRegexes=[r'I|V|X|L|C|D|M+', 'zero'])  # allow certain Regexes, + means one or more
response = pyip.inputNum(blockRegexes=[r'[02468]$'])  # block regexes that end with 02468
response = pyip.inputStr(allowRegexes=[r'caterpillar', 'category'], blockRegexes=[r'cat'])


# CUSTOM FUNCTION
def addsUptoTen(numbers):
    numbersList = list(numbers)  # converts number to list
    for i, digit in enumerate(numbersList):  # 'enumerate' assigns indexes to its values in the (list)
        numbersList[i] = int(digit)  # converts value to integer, then assigns value to corresponding index
    if sum(numbersList) != 10:  # if the sum of the numbers is not 10 ...
        raise Exception('The digits must add up to 10, not %s.' % (sum(numbersList)))
        # ... print message, raise exception
    return int(numbers)


response = pyip.inputCustom(addsUptoTen)  # also allows for blank, limit, etc.
