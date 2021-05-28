# Write a Python program to subtract five days from current date.
# Sample Date :
# Current Date : 2015-06-22
# 5 days before Current Date : 2015-06-17

# fecha = datetime.strptime(string_date, "%b %d %Y %I:%M%p")

import datetime


def delta_date(date_str, days_delta):
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    new_date = date + datetime.timedelta(days=days_delta)
    return new_date.strftime("%Y-%m-%d")


print(delta_date("2015-06-22", -5))


def cambiarfecha(fecha, cambiarsemana):
    date = datetime.datetime.strptime(fecha, "%Y-%m-%d")
    cambiarporsemanas = date + datetime.timedelta(days=cambiarsemana)
    print(cambiarporsemanas)


fecha = input("digite una fecha Año-Mes-Dia: ")
cambiar = int(input("digite numero de semanas a cambiar: "))
cambiarfecha(fecha, cambiar)
