# Write a program that asks for the user for the month number
# your script should convert the number to the month's name and prints it

# month_number = input("Insert a month number: ")
# month_number = float(month_number)

# Solution 1

num= float(input("Ingrese el numero del mes : "))
# if num == 1:
#     print("Mes de Enero")
# elif num == 2:
#     print("Mes de Febrero")
# elif num == 3:
#     print("Mes de Marzo") 
# elif num == 4: 
#     print("Mes de Abril") 
# elif num == 5: 
#     print("Mes de Mayo") 
# elif num == 6: 
#     print("Mes de Junio") 
# elif num == 7: 
#     print("Mes de Julio") 
# elif num == 8: 
#     print("Mes de Agosto") 
# elif num == 9: 
#     print("Mes de Septiembre") 
# elif num == 10: 
#     print("Mes de Octubre") 
# elif num == 11: 
#     print("Mes de Noviembre") 
# elif num == 12: 
#     print("Mes de Diciembre")
# else:
#     print("Error número ingresado")

# Solution 2

# if num not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
#     print("No valido")
# elif num == 1:
#     print("Mes de Enero")
# elif num == 2:
#     print("Mes de Febrero")

# Solution 3

# if num in range(1, 13):
#     print("No valido")
# elif num ==1:
#     print("Enero")
# .
# .
# .

my_dict = {1: "enero", 2: "febrero"}

if num not in range(1, 13):
    print("No es valido")
else:
    print(my_dict[num])

# Solution 4

indexes = list(my_dict.keys())

if num not in indexes:
    print("No valido")
else:
    print(my_dict[num])
