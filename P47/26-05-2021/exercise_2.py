# Write a Python program to convert a string to datetime.
# Sample String : Jan 1 2014 2:43PM
# Expected Output : 2014-07-01 14:43:00

import datetime

# Solution 1
def convert_date(date_str):
    date = datetime.datetime.strptime(date_str, "%b %d %Y %I:%M%p")
    new_date = date.strftime("%Y-%m-%d %H:%M:%S")
    return new_date

new_date = convert_date("Jan 1 2014 2:43PM")
print(new_date)

#Solution 2
date = datetime.datetime.strptime("Jan 1 2014 2:43PM", "%b %d %Y %I:%M%p")
print(date)
