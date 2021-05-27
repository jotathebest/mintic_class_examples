# Write a Python program to subtract five days from current date.
# Sample Date :
# Current Date : 2015-06-22
# 5 days before Current Date : 2015-06-17
import datetime


def date_time_delta(date_str, delta_days):
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    new_date = date + datetime.timedelta(days=delta_days)
    return new_date.strftime("%Y-%m-%d")


print(date_time_delta("2015-06-22", 5))
