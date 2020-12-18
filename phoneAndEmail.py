#! python3
# phoneAndEmail.py - finds phone numbers and email addresses on the clipboard


import pyperclip, re


# PHONE NUMBER REGEX
# this code is to DETECT all forms of a phone number
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?  # area code - matches 3 digits OR 3 digits with parentheses (optional)
(\s|-|\.)?  # separator - matches space OR dash OR dot (optional)
(\d{3})  # first 3 digits
(\s|-|\.)  # separator - matches space OR dash OR dot
(\d{4})  # last 4 digits 
(\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension - matches space (zero or none), (ext OR x OR ext.), space (zero or none), 
2 to 5 digit number sequence (optional)
)''', re.VERBOSE)

# EMAIL REGEX
emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+  # matches all letters, upper or lowercase, numbers, and punctuation - "thomasngn673"
@  # @ symbol - "@"
[a-zA-Z0-9.-]+ # domain name - "gmail"
(\.[a-zA-Z]{2,4})  # ".com"
)''', re.VERBOSE)

# this code gathers all detected phone numbers and reorders them as a list of uniformly formatted phone numbers
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):  # find each group/part of phone numbers
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])  # joins 10 digit phone number with no space, dashes, etc.
    if groups[8] != '':  # if extension is not blank ...
        phoneNum += ' x' + groups[8]  # ... phoneNum = phoneNum x'extension'
    matches.append(phoneNum)  # add phoneNum to matches
for groups in emailRegex.findall(text):  # find email addresses (only one group/part, so joining is not needed)
    matches.append(groups[0])  # groups(0) and groups() match the entire expression

# COPY TO CLIPBOARD
if len(matches) > 0:  # if there are more than 1 match ...
    pyperclip.copy('\n'.join(matches))  # ... copy to clipboard (newline, every match)
    print('Copied to clipboard.')
    print('\n'.join(matches))  # print newline every match
else:
    print('No phone numbers or email addresses found.')
