# Write a program that asks for the user for the month number
# your script should convert the number to the month's name and prints it

# Solution 1

# month_number = input("Insert a month number: ")
# month_number = int(month_number)

# months = {"1": "enero", "2": "febrero", "3": "marzo"}

# if month_number < 1 or month_number > 12:
#     print("you inserted a not valid number")
# else:
#     month = months[str(month_number)]
#     print(month)

# # Solution 2

# month_number = input("Insert a month number: ")
# month_number = int(month_number)
# months = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", 
#           "octubre", "noviembre", "diciembre"]
# # 0
# # 1

# if month_number < 1 or month_number > 12:
#     print("you inserted a not valid number")
# else:
#     month_number = month_number - 1
#     print(months[month_number])

# # Solution 3

month_number = input("Insert a month number: ")
month_number = int(month_number)
months = ["", "enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", 
          "octubre", "noviembre", "diciembre"]

# 1
# False and False
# False

# -1
# True and False
# False
if month_number < 1 or month_number > 12:
    print("you inserted a not valid number")
else:
    print(months[month_number])


