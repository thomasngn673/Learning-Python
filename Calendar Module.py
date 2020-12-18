import calendar

print(calendar.weekheader(3))
# number in parentheses is length of characters
print()

print(calendar.firstweekday())
# first day of the week is Monday, starts counting at 0
print()

print(calendar.month(2020,5,3,1))
# calendar.month(year, # of month, # of characters of weekdays, length between rows)
print()

print(calendar.monthcalendar(2020,5))
# gives in matrix form
print()

print(calendar.calendar(2020))
print()

day_of_the_week = calendar.weekday(2020,5,18)
print(day_of_the_week)
print()

is_leap = calendar.isleap(2020)
print(is_leap)
print()

how_many_leap_days = calendar.leapdays(2000,2020)
print(how_many_leap_days)
print()