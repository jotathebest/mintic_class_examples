import datetime

date = datetime.date.today()
# print(date)
# print(date.year, date.month, date.day)
# print(date.isoformat())

date = datetime.datetime.now()
print(date)
print(date.hour, date.minute)
print(date.strftime("%y/%B/%d"))
