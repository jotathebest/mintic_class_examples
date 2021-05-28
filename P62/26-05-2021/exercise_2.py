# Write a Python program to convert a string to datetime.
# Sample String : Jan 1 2014 2:43PM
# Expected Output : 2014/01/01 14:43:00

# strptime()

import datetime


# def convert_date(date_str):
#     date = datetime.datetime.strptime(date_str, "%b %d %Y %I:%M%p")
#     return date.strftime("%Y-%m-%d %H:%M:%S")

# print(convert_date("Jan 1 2014 2:43PM"))


from datetime import datetime

string_date = input("Escribe la fecha: ")


def convertir_fecha(string_date):
    fecha = datetime.strptime(string_date, "%b %d %Y %I:%M%p")
    return fecha


print(convertir_fecha(string_date))
