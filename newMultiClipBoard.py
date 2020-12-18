#! newMultiClipBoard.py
# newMultiClipBoard - allows user to add/update pasted information instead of replacing it

# Usage of this module:
# py.exe mcb.pyw save <keyword> - saves clipboard to keyword
# py.exe mcb.pyw <keyword> - loads text associated with keyword to clipboard
# py.exe mcb.pyw list - loads all keywords to clipboard
# py.exe mcb.pyw delete <keyword> - deletes a keyword from the shelf
# py.exe mcb.pyw delete - delete all keywords

# SYS.ARGV IS THE TEXT IN THE COMMAND LINE

import sys, pyperclip, shelve

# Open file
mcbShelf = shelve.open('mcb')

# Write into file
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        # if the length of the text on the command line is 3 words & the second word of the text is 'save'
        # .lower() returns the string text as lowercase
        mcbShelf[sys.argv[2]] = pyperclip.paste()  # paste clipboard to the keyword (3rd word of the text)
    elif sys.argv[1].lower() == 'delete':
        del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:  # if the length of the text is only 2 ...
    if sys.argv[1] == 'list':  # if the 2nd word in the text is 'list' ...
        pyperclip.copy(str(list(mcbShelf.keys())))  # ... copy all keywords to clipboard
        # mcbShelf.keys() are the keywords, mcbShelf.values() are the original copied content
    elif sys.argv[1] in mcbShelf:  # if the keyword is in the shelf ...
        pyperclip.copy(mcbShelf[sys.argv[1]])  # ... copy the text associated with keyword to clipboard
    elif sys.argv[1] == 'delete':
        mcbShelf.clear()

# Close file
mcbShelf.close()