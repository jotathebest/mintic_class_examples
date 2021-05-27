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

#a)
date=datetime.datetime.now()
print(date)
#b)
print(date.year)
#c)
print(date.month)
#d
print(date.strftime("%U"))
#e)
print(date.strftime("%W"))
#f)
print(date.strftime("%j"))
#g)
print(date.day)
#h)
print(date.strftime("%A")) 
