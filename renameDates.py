import re, os, shutil

# renames filenames with american format MM-DD-YYYY to european format DD-MM-YYYY

# CREATE REGEX FOR IDENTIFYING AMERICAN DATES
# there may be some invalid dates
americanDate = re.compile(r"""^(.*?)  # all text before the date 
((0|1)?\d)-  # one digit \d (1-9) OR two digit (0|1)\d starting with 0\d or 1\d
# (.) matches any character except newline
# (*) any number of times
# (?) non-greedy regex
((0|1|2|3)?\d)-  # one digit \d (1-9) OR two digit starting with 0\d, 1\d, 2\d, 3\d
((19|20)\d\d)  # four digit starting with 19|20, (19)\d\d OR (20)\d\d
(.*?)$  # all text after the date
""", re.VERBOSE)  # verbose ignores space, comments

# LOOP OVER ALL FILES IN THE DIRECTORY
for amerFileName in os.listdir('.'):  # print all files and folders in path '.'
    mo = americanDate.search(amerFileName)  # match regex pattern for every single file, assign to 'mo'

    # SKIP FILES WITHOUT A DATE
    if mo is None:  # if 'mo' does not match with the specified file
        continue  # continue goes through to the next 'for loop'

    # GET DIFFERENT PARTS OF FILENAME
    beforeText = mo.group(1)
    month = mo.group(2)  # group(2) encompasses everything in the parentheses, even group(3); (2(3))
    day = mo.group(4)  # (4(5))
    year = mo.group(6)  # (6(7))
    afterText = mo.group(8)  # (8(9))

    # REFORMAT TO EUROPEAN DATE
    europeanDate = beforeText + day + '-' + month + '-' + year + afterText

    # GET ABSOLUTE FILE PATHS - MUST use shutil.move, cannot change variable name by using equal sign
    # abspath() writes code to the current working directory which is /Users/thomasnguyen/Desktop
    # the desired result is /Users/thomasnguyen/Desktop/Python/folderName
    absWorkingDir = os.path.abspath('.')
    # Join files into absolute directory
    amerFileName = os.path.join(absWorkingDir, amerFileName)
    euroFileName = os.path.join(absWorkingDir, europeanDate)

    # RENAME THE FILES
    print(f'Renaming "{amerFileName}" to "{euroFileName}" ...')
    shutil.move(amerFileName, euroFileName)  # moving amerFileName to destination euroFileName will replace it
