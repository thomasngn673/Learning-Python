# CONVERT AN ENGLISH MESSAGE INTO PIG LATIN
# Pig Latin Rules:
# 1. Word begins with a vowel, add "yay" to the end of it
# 2. Word begins with consonant or consonant cluster, move to the end of the word and add "ay"

message = input('Enter the English message to translate into Pig Latin.\n')  # asks for message input
VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']
pigLatin = []  # create new list to join later

for word in message.split():  # splits the message into a list of tuples, loops through every word in the list

    # Separate the non-letters at the start of this word (punctuation):
    prefixNonLetters = ''  # create character list for non letter prefixes
    while len(word) > 0 and not word[0].isalpha():  # while length of word >0 and first character is not a letter ...
        prefixNonLetters += word[0]  # ... add the character to prefixNonLetters
        word = word[1:]  # assign remaining characters in word as new word to loop back again
        # "filters" out non-letter characters to move the word through the following conditions
    if len(word) == 0:  # in the case that the original word was just a single non-letter ...
        pigLatin.append(prefixNonLetters)  # ... add the character to pigLatin list as it is
        continue

    # Separate the non-letters at the end of this word (punctuation):
    suffixNonLetters = ''  # create character list for non letter suffixes
    while not word[-1].isalpha():  # while the last character of the word is a not a letter ...
        suffixNonLetters += word[-1]  # ... add the character to prefixNonLetters
        word = word[:-1]  # new word is free of non-letter characters before and after it

    # Remember if the word was in uppercase or title case.
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower()  # Make the word lowercase for translation.

    # Separate the consonants at the start of this word:
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:  # if length of word >0 and first character is a consonant ...
        prefixConsonants += word[0]  # ... add the consonant to prefixConsonants
        word = word[1:]  # assigns new word that doesn't have consonants at the beginning

    # Add the Pig Latin ending to the word:
    if prefixConsonants != '':  # if prefixConsonants is not empty ...
        word += prefixConsonants + 'ay'  # new word = (prior word with no letters before and after, and no consonants
        # at the beginning) + consonant + 'ay'
    else:  # if prefixConsonants contains nothing ...
        word += 'yay'  # ... add "yay" to the end

    # Set the word back to uppercase or title case:
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    # Add the non-letters back to the start or end of the word
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

    # loops until entire message is read

# Join all the words back together into a single string:
print(' '.join(pigLatin))