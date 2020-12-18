import shutil, os
from pathlib import Path

# MOVING FILES
p = Path.home()
shutil.copy(p/'spam.txt', p/'some_folder')  # copies the spam.txt file to 'some_folder'
shutil.copytree(p/'spam', p/'spam_backup')  # creates new folder 'spam_backup' with same contents as folder 'spam'
shutil.move('C://bacon.txt','C://eggs')  # moves bacon.txt to eggs folder
# if eggs folder doesn't exist, bacon.txt is renamed as 'eggs'
shutil.move('C://bacon.txt','C://eggs//new_bacon.txt') # moves bacon.txt to eggs folder and rename as new_bacon.txt

# DELETING FILES AND FOLDERS
os.unlink(p)  # delete file at path 'p' /Users/thomasnguyen/Desktop/Python/eggs/spam.txt
os.rmdir(p)  # delete folder at path 'p' /Users/thomasnguyen/Desktop/Python/eggs
# there must be no files within the path to successfully delete it
shutil.rmtree(p)  # deletes files and folders at path 'p'

# SEND TO TRASH MODULE
import send2trash
baconFile = open('bacon.txt','a')  # creates the file
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
send2trash.send2trash('bacon.txt')  # send .txt file to the trash bin

# WALKING A DIRECTORY TREE
for folderName, subFolders, fileNames in os.walk('C://delicious'):
    print('The current folder is '+folderName)

    for subFolder in subFolders:
        print('The subfolder of '+folderName+'is '+subFolder)

        for fileName in fileNames:
            print('The file inside '+folderName+' '+fileName)

    print('')
# This code lists - all subfolders of current folder
# - all files in each subfolder, one by one
# os.walk () returns:
# 1. string of current folder's name
# 2. list of strings of the folders in the current folder
# 3. list of strings of files in the current folder

# READING ZIP FILES
import zipfile
from pathlib import Path
p = Path.home()
exampleZip = zipfile.ZipFile(p/'example.zip')  # unzips example.zip file in path, assigns to variable
exampleZip.namelist()  # lists all files/folders in zip

# EXTRACTING ZIP FILES
exampleZip = zipfile.ZipFile(p/'example.zip')
exampleZip.extractall()  # files will be extracted to default C:/
exampleZip.extractall('C://delicious')  # files will be extracted to 'delicious'
exampleZip.close()

exampleZip.extract('spam.txt','C://some//new//folders')  # .extract extracts only specified file
# single file extracted to specified path

# CREATING AND ADDING TO ZIP FILES
newZip = zipfile.ZipFile('new.zip','w')  # create new zip file called new.zip
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)  # write a spam.txt file into the zip
newZip.close()