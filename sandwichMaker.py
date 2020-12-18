import pyinputplus as pyip

cost = 0  # set cost = 0

breadChoices = {'Wheat': float(2), 'White': float(1.5), 'Sourdough': float(2.5)}  # create dict of bread choices
breadResponse = pyip.inputMenu(['Wheat', 'White', 'Sourdough'], caseSensitive=False)
cost = cost + breadChoices[str(breadResponse)]  # calls on value in dictionary breadchoice[breadtype] gives value

proteinChoices = {'Chicken': float(.5), 'Turkey': float(1.5), 'Ham': float(1.0), 'Tofu': float(.75)}  # create dict
# of protein choices
proteinResponse = pyip.inputMenu(['Chicken', 'Turkey', 'Ham', 'Tofu'], caseSensitive=False)
cost = cost + proteinChoices[str(proteinResponse)]

cheeseDecision = pyip.inputYesNo('Would you like cheese on your sandwich?\n', caseSensitive=False)
if cheeseDecision != 'no':  # inputYesNo only allows yes/no, if answer is not no then give options for cheese
    cheeseChoices = {'Cheddar': float(.25), 'Swiss': float(.25), 'Pepperjack': float(.40)}  # create dict of cheese
    # choices
    cheeseResponse = pyip.inputMenu(['Cheddar', 'Swiss', 'Pepperjack'], caseSensitive=False)
    cost = cost + cheeseChoices[str(cheeseResponse)]

condimentDecision = pyip.inputYesNo('Would you like condiments on your sandwich?\n', caseSensitive=False)
if condimentDecision != 'no':  # inputYesNo only allows yes/no, if answer is not no then give options for condiments
    condimentChoices = {'Mayo': float(.10), 'Mustard': float(.10), 'Lettuce': float(.50), 'Tomatoes': float(.50)}
    # create dict of condiment choices
    condimentResponse = pyip.inputMenu(list(condimentChoices.keys()), caseSensitive=False)
    cost = cost + condimentChoices[str(condimentResponse)]

sandwichQuantity = pyip.inputInt('How many sandwiches would you like?\n')
cost = cost * sandwichQuantity

print('Your total is: $' + str(cost))
