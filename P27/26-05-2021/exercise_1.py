# Write a Python script to display the various Date Time formats
# a) Current date and time
# b) Current year
# c) Month of year
# d) Week number of the year
# e) Weekday of the week
# f) Day of year
# g) Day of the month
# h) Day of week

import datetime
date = datetime.datetime.now()
print(f"current date and time: {date}")
print(f"current year: {date.year}")
print(f"month year: {date.strftime('%B')}")
print(f"week number of the year: {date.strftime('%U')}")
print(f"Weekday of the week: {date.strftime('%w')}")
print(f"Day of year: {date.strftime('%j')}")
print(f"Day of month: {date.strftime('%d')}")
print(f"Day of week: {date.strftime('%A')}")
