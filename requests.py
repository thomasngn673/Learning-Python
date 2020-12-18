# RUN IN PYTHON CONSOLE
import requests

res = requests.get('http://automatetheboringstuff.com/files/rj.txt')

# DOWNLOAD SUCCESS CHECK METHOD 1
type(res)
res.status_code == requests.codes.ok  # res.status_code gives code of the request
# requests.codes.ok is the request code for HTTP and belongs to a list of other request codes,
# request codes are a feedback of some sort
# by res.status_code == requests.codes.ok, we are checking if the codes are the same, and if our custom input code is
# matched with the HTTP code

# DOWNLOAD SUCCESS CHECK METHOD 2
res.raise_for_status()

len(res.text)
print(res.text[:250])

# SAVE DOWNLOADED FILES TO HARD DRIVE
playFile = open('RomeoAndJuliet.txt','wb')
# must open file in 'write binary' mode
for chunk in res.iter_content(100000):  # write into the file in increments so as to not overload the download module
    playFile.write(chunk)
playFile.close()