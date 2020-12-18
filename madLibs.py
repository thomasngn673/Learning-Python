from pathlib import Path
import os, re
from pathlib import Path

# Original MadLib file is created
if not os.path.isdir(Path.home()/'Desktop'/'Python'/'madLibs'):  # if the path doesn't already exist ...
    os.makedirs(Path.home()/'Desktop'/'Python'/'madLibs')  # ... create a directory for MadLibs
os.chdir(Path.home()/'Desktop'/'Python'/'madLibs')  # change default directory to drop txt file in
textFile = open(f'textFile.txt', 'w')  # write file named textFile
textFile.write('The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.')
textFile.close()

# Original MadLib file is opened and read
origText = open('textFile.txt', 'r')
textOrig = origText.read()
origText.close()

# re. is used to search the text
splitText = re.compile('\w+|\s+|[^\w\s]')  # matches with any word OR space OR anything that isn't a word/space
# (punctuation)
splitText = splitText.findall(textOrig)  # txt file is searched, split and placed into a list

articles = ['ADJECTIVE', 'NOUN', 'VERB', 'ADVERB']
for i in range(len(splitText)):
    for j in range(len(articles)):
        if splitText[i] == articles[j]:  # if item in splitText is equal to item in articles
            splitText[i] = input('Enter a(n) ' + ((articles[j]).lower()) + ':\n')
            # replace the splitText value with inputted value
newText = ''.join(splitText)  # join all items in the list into a sentence
newTextFile = open(f'newTextFile','w')  # create new file in file path
newTextFile.write(newText)  # write newText into new file
newTextFile.close()  # close newTextFile
