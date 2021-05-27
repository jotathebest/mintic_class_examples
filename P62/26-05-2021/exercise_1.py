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

def print_dates():
    date = datetime.datetime.now()
    print(date)
    print(date.year)
    print(date.month)
    print(date.strftime("%b"))
    print(date.strftime("%U"))
    print(date.strftime("%j"))
    print(date.strftime("%d"))
    print(date.strftime("%A"))

print_dates()
