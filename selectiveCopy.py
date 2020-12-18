import os, shutil

folder = input('Enter the path of the folder you would like to search through.')
fileType = input('Enter the file type extension you would like to search.')
newDestination = input('Enter the new destination of the file you want to search for.')

for foldername, subfolders, filenames in os.walk(folder):  # lists 3 things, write code to specify thing that we want
    for filename in filenames:  # looks at all the files in the folder
        if filename.endswith('{}'.format(fileType)):  # if file ends with specified file type...
        # .format(variable) assigns variable to the {} before it, similar to f' string
            shutil.move(os.path.join(foldername, filename), newDestination)
            # shutil.move requires (path, newPath)
            # os.path.join(foldername, filename) creates the 'path'
            # shutil.move(filename,newDestination) doesn't work because filename is not a valid path

print('All files of file type '+fileType+' have been copied from'+os.path.basename(folder)+' to '+os.path.basename(newDestination))