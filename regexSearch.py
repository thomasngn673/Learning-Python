from pathlib import Path
import os, re


# Create .txt Files
if not os.path.isdir(Path.home()/'Desktop'/'Python'/'regexSearch'):
    os.makedirs(Path.home()/'Desktop'/'Python' /'regexSearch')

os.chdir(Path.home()/'Desktop'/'Python'/'regexSearch')

textFile1 = open(f'textFile1.txt', 'w')
textFile1.write('8329888563832212697883221270678329888566')
textFile1.close()

textFile2 = open(f'textFile2.txt', 'w')
textFile2.write('8322126978832212706783298885662818447729')
textFile2.close()

textFile3 = open(f'textFile3.txt', 'w')
textFile3.write('83221269788322127067832988856628184477298329888563')
textFile3.close()


# Create search function
def search(regex, txt):
    searchRegex = re.compile(regex, re.I)  # matches regex (which is later defined by input function), ignore
    # lower/uppercase
    result = searchRegex.findall(txt)  # search txt for regex
    print(result)  # print result

# Check that directory user is searching exists
# /Users/thomasnguyen/Desktop/Python/regexSearch
while True:
    dirs = input('Enter the absolute path of the folder that you want to search:\n')
    if os.path.exists(dirs) == True:
        print('This folder exists')
        break
user_search = input('Enter the regular expression:\n')

folder = os.listdir(dirs)  # list all files within the inputted directory

for file in folder:
    if file.endswith('.txt'):
        print(os.path.join(dirs, file))  # print the path that end with the file name .txt
        txtfile = open(os.path.join(dirs, file), 'r+')  # opens the .txt file within the path
        msg = txtfile.read()  # assigns variable to text within the .txt file
        search(user_search, msg)  # custom function