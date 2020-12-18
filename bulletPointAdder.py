#! python3
# bulletPointAdder.py - adds Wikipedia bullet points to the start of each line of text on the clipboard

import pyperclip

text = pyperclip.paste()
# paste paragraph of lines

# separate lines and add stars
lines = text.split('\n')
# creates list of all the lines
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]  # adds a star to each index of each line

text = '\n'.join(lines)  # joins entire list separated by new lines
pyperclip.copy(text)