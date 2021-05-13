# Write a program that asks for the user for the month number
# your script should convert the number to the month's name and prints it

month_number = input("Insert a month number: ")

# Solution 1

months = {1:"Januar", 2:"Februar", 3:"March", 4:"April", 5:"May", 6:"Juny", 7:"July", 8: "August", 9:"September", 10:"October", 11:"November", 12:"December"}

month_number = input ("Please insert a month number: ")

if int(month_number) < 1 or int(month_number)>12:
    print("Please type a correct month number") 
else:
    month_number=int(month_number)
    print(months[month_number])

# Solution 2

n=input("inserte numero del mes: ")
n=int(n)
my_year=[ " ", "ene", "feb", "mar", "abr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dic"]
if n>=1 and n<=12:
    print(my_year[n])
else:
    print("not valid") 

# Solution 3

n=input("inserte numero del mes: ")
n=int(n)
my_year=["ene", "feb", "mar", "abr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dic"]
if n>=1 and n<=12:
    n = n -1
    print(my_year[n])
else:
    print("not valid") 

# Solution 4

month_number = int(input("Insert a month number: "))
def validate_month(month): 
    if month == 1: 
        return "January" 
    elif month == 2: 
        return "February" 
    elif month == 3: 
        return "March" 
    elif month == 4: 
        return "April" 
    elif month == 5:
        return "May"
    elif month == 6:
        return "June"
    elif month == 7:
        return "July"
    elif month == 8:
        return "August"
    elif month == 9:
        return "September"
    elif month == 10:
        return "October"
    elif month == 11: 
        return "November"
    elif month == 12:
        return "December"
    return "Insert a valid number"

print(validate_month(month_number)) 
