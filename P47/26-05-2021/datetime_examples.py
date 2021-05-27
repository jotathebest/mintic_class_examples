import datetime

date = datetime.date.today()
print(date.year, date.month, date.day)

date = datetime.datetime.now()
print(date.year, date.month, date.day, date.hour, date.minute, date.second, date.microsecond)

print(date.strftime("%I"))
