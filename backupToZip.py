#! python3
# backupToZip.py - copies entire folder and its contents into a ZIP file
import zipfile, os

def backupToZip(folder):
    folder = os.path.abspath(folder)  # make sure folder is absolute

    number = 1
    while True:
        zipFilename = os.path.basename(folder)+'_'+str(number)+'.zip'
        if not os.path.exists(zipFilename):  # the first time this loops, file will not exist, so it will break the
            # while loop
            break
        number = number + 1
        # second time it loops number is increased
        # the path will not exist however, because it needs to be passed through the functions below, so it will break
        # again

    print(f'Creating {zipFilename}...')  # prints creation of the name of the zipfile
    backupZip = zipfile.ZipFile(zipFilename,'w')  # create the actual zipfile in 'write' mode

    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')
        backupZip.write(foldername)  # write all folders into zipfile

        # Check for duplicates and only add new files
        for filename in filenames:  # loops through all the files in the folder
            newBase = os.path.basename(folder)+'_'
            if filename.startswith(newBase) and filename.endswith('.zip'):  # if zip file already exists, go to next
                # iteration of the 'for' loop
                continue
            backupZip.write(os.path.join(foldername,filename))  # if it doesn't exist yet, write into the backupZip
        backupZip.close()
        print('Done.')