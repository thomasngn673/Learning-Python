import os


folder = input('Enter the absolute path of the folder you want to delete large files from.\n')
byteSize = int(input('Enter the file size, in bytes, of files larger than this number to be deleted.\n'))
for roots, dirs, filenames in os.walk(folder):
    for filename in filenames:
        fileSize = os.path.getsize(folder)
        if fileSize > byteSize:
            print(filename+' is a large file, with '+str(fileSize)+'bytes of data.')