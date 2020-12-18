import os, re, shutil

folder = input('Enter the absolute path of the folder you would like to fill in the gaps with.')
filePattern = re.compile(r'^(spam)(\d+)(.txt)')  # starts with spam(digits one or more).txt

lst = []
for file in os.listdir(folder):  # lists all files in 'folder', ex. spam001.txt
    num = filePattern.search(file).group(2)  # search each file in 'folder' for regex, (\d+) is variable 'num'
    lst.append((int(num.lstrip('0')), file, len(num)))
    # num.lstrip('0') removes all '0' from leading characters of 'num' --> non-zero remaining numbers are converted to
    # 'int'
    # add to list ((remaining non-zero), file name, length of 'num' with zeros)
    # ex. spam001.txt, lst = [[1, spam001.txt, 3]...]

lst = sorted(lst)  # sorted() reorders numbers numerically
# lst is rearranged numerically by remaining non-zero numbers
# ex. spam001.txt in lst[[1,spam001.txt,3]...]
for index in range(len(lst)):  # loops through number of files in 'folder'
    padding = lst[index][2]  # assigns 'padding' to every len(num) of every file, ex. padding = 3
    num = str(int(index)+1)  # reassigns 'num' to (index #)+1, ex. num = 1, assuming this is the 1st loop
    padded_num = num.rjust(int(padding), '0')
    # .rjust(length,character) returns 'num' with length 'padding' # of characters, and replace with 'character'
    # num = 1, padding = 3, padded_num = 001
    src = os.path.join(folder, lst[index][1])  # add 'spam001.txt' to folder
    dst = os.path.join(folder, filePattern.sub(r'\g<1>%s\g<3>' % padded_num, lst[index][1]))
    # .sub previous regex
    # \g<1> is group 1, \g<3> is group 3, %s replaces previous (\d+)
    shutil.move(src, dst)