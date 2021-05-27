# Write a Python program to convert a string to datetime.
# Sample String : Jan 1 2014 2:43PM
# Expected Output : 2014-07-01 14:43:00


import datetime


def transform_date(date_str):
    date = datetime.datetime.strptime(date_str, "%b %d %Y %I:%M%p")
    new_date = date.strftime("%Y-%m-%d %H:%M:%S")
    return new_date


print(transform_date("Jan 1 2014 2:43PM"))
