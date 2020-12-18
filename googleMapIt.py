#! python3
# googleMapIt.py - launches a map in the browser using an address from the command line/clipboard

import webbrowser, sys, pyperclip
if len(sys.argv)>1:  # if the length of the text in the command line is greater than 1...
    address = ' '.join(sys.argv[1:])
    # sys.argv[0] is googleMapIt
    # sys.argv[1:] is 17134 Fairway Glen Ct. Sugar Land, TX
    # address is joined by a space, ' '
else:  # if the length of the text in the command line is NOT greater than 1...
    address = pyperclip.paste()  # get address from text already in clipboard

webbrowser.open('https://www.google.com/maps/place/'+address)