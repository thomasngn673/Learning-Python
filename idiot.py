import pyinputplus as pyip


while True:
    response = pyip.inputYesNo('Want to know how to keep an idiot busy for hours?\n')
    if response == 'no'|'No':
        break
        print('Thank you. Have a nice day.')
