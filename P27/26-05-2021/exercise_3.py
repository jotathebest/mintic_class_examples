# Write a Python program to subtract five days from current date.
# Sample Date :
# Current Date : 2015-06-22
# 5 days before Current Date : 2015-06-17


import datetime


def delta_time(date_str, days_input):
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    new_date = date + datetime.timedelta(days=days_input)
    return new_date.strftime("%Y-%m-%d")


print(delta_time("2015-06-22", 5))
