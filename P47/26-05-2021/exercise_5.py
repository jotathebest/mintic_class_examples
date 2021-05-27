# Write a Python program to get days between two dates. Go to the editor
# Sample Dates : 2000,2,28, 2001,2,28
# Expected Output : 366 days, 0:00:00

import datetime


def get_number_of_days(date_1, date_2):
    date_1 = datetime.datetime.strptime(date_1, "%Y,%m,%d")
    date_2 = datetime.datetime.strptime(date_2, "%Y,%m,%d")
    result = date_2 - date_1
    return result.days


days = get_number_of_days("2000,2,28", "2001,2,28")
print(f"{days} days")
