import re

text = input('Input text for data detection.\n')
dateRegex = re.compile(r'(\d{2}|\d)/(\d{2}|\d)/(\d{4})')
# matches with (2 digits OR 1 digit)/(2 digits OR 1 digit)/(4 digits)

matches = []

# create list for days 1-31
dayRange31 = []
for i in range(1, 32):
    if i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:  # if int is single digit ...
        i = '0' + str(i)  # ... add a '0' in front of it
    if i in [*range(10, 32)]:  # [10-31] doesn't work, [*range(10,31)]
        i = str(i)
    dayRange31.append(i)

# create list for days 1-30
dayRange30 = []
for i in range(1, 31):
    if i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        i = '0' + str(i)
    if i in [*range(10, 31)]:  # [10-31] doesn't work, [*range(10,31)]
        i = str(i)
    dayRange30.append(i)

# create list for months 1-12
monthRange = []
for i in range(1, 13):
    if i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        i = '0' + str(i)
    if i in [*range(10, 13)]:
        i = str(i)
    monthRange.append(i)

# create list for days 1-28
dayRange28 = []
for i in range(1, 29):
    if i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        i = '0' + str(i)
    if i in [*range(10, 29)]:  # [10-31] doesn't work, [*range(10,31)]
        i = str(i)
    dayRange28.append(i)

# create list for days 1-29
dayRange29 = []
for i in range(1, 30):
    if i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        i = '0' + str(i)
    if i in [*range(10, 30)]:  # [10-31] doesn't work, [*range(10,31)]
        i = str(i)
    dayRange29.append(i)

# create list for years 1000-2999
yearRange = []
for i in range(1000, 3000):
    i = str(i)
    yearRange.append(i)

# create list for every leap year 1000-2999
leapYearRange = []
for i in range(1000, 2999):
    if i % 4 == 0:  # if year is divisible by 4 ...
        if i % 100 == 0:  # (1) ... and divisible by 100 and DOESN'T WORK
            pass  # ... INVALID
            if i % 400 == 0:  # ... UNLESS divisible by 400
                leapYearRange.append(str(i))
        else:  # (2) ... and is not divisible by 100 and WORKS
            leapYearRange.append(str(i))  # ... VALID

for dates in dateRegex.findall(text):
    fullDate = '/'.join([dates[0], dates[1], dates[2]])  # join groups into fulldate
    # test if dates are in general range - broad verification
    if dates[0] in dayRange31:  # if day is from 1-31 ...
        if dates[1] in monthRange:  # if month is from 1-12 ...
            if dates[2] in yearRange:  # if year is from 1000-2999 ...

                # test if dates are valid
                # April, June, September, November have 30 days only
                if (int(dates[1]) == int(monthRange[3])) | (int(dates[1]) == int(monthRange[5])) | (int(dates[1]) ==
                                                        int(monthRange[8]) | (int(dates[1]) == int(monthRange[10]))):
                    # if the month is April, June, September, or November ...
                    if dates[0] in dayRange30:  # ... and if days are within 30
                        matches.append(fullDate)
                        continue  # 'CONTINUE' RESTARTS THE FOR LOOP, 'BREAK' BREAKS OUT OF ENTIRE LOOP,
                        # 'PASS' GOES ONTO NEXT LOOP
                    else:  # ... if days are not within 30, it is invalid
                        print('Invalid date: ' + fullDate + '.' + ' Days in this month can\'t exceed 30 days.')

                # February
                if dates[1] == monthRange[1]:  # if month is February ...
                    if (dates[2]) in leapYearRange:  # ... and it is a leap year and has days within 28 days ...
                        if (dates[0]) in dayRange28:  # ... and has 28 days
                            matches.append(fullDate)
                            continue
                        else:  # if it doesn't have 28 days
                            print('Invalid date: ' + fullDate + '.' ' In a leap year, February has 28 days.')
                            continue
                    if ((dates[2]) in yearRange) & (dates[2] not in leapYearRange):  # ... and it is a non-leap year ...
                        if dates[0] in dayRange29:  # ... and has 29 days
                            matches.append(fullDate)
                            continue
                        else:  # if it doesn't have 29 days
                            print('Invalid date: ' + fullDate + '.' ' In a non-leap year, February has 29 days.')
                            continue
                matches.append(fullDate)

if len(matches) == 0:  # if there are no matches, print following message
    print('There were no valid dates found within the text.')
else:  # if there is a match, print the match
    print(matches)