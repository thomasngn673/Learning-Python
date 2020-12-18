#! python3
# mclip.py - A multi-clipboard program.

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python3 mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]  # first command line arg is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)

# TERMINAL INSTRUCTIONS
# 1. open terminal
# 2. cd = change directory
# 3. type "cd PycharmProjects/Summer2020_python"
#       - essentially change to directory wherever desired .py file is
# 4. python3 mclip.py
#       - brings up 'Usage: py mclip.py [keyphrase]'
# 5. python3 mclip.py [keyphrase]
#       - either copies to clipboard or prints 'There is no text'

# sys.argv seems to be the variable after 'python3 filename.py'
