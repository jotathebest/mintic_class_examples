# https://www.hackerrank.com/challenges/write-a-function/problem?h_r=internal-search

# Solution 1

year = input("Insert a year: ")
year = int(year)

if not year % 4 == 0:
    print("No es bisiesto")
elif not year % 100 == 0:
    print("Es bisiesto")
elif not year % 400 == 0:
    print("no es bisiesto")
else:
    print("es bisiesto")

# Solution 2

year=int(input("Enter year: "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("es bisiesto")
        else: print("no es bisiesto")
    else: print("es bisiesto")
else: print("No es bisiesto")

# Solution 3

year=input("Year? ")
year=int(year)
if year%4!=0:
    print("El año no es bisiesto")
elif year%4==0 and year%100!=0:
    print("El año es bisiesto")
elif year%4==0 and year%100==0 and year%400!=0:
    print("El año no es bisiesto")
elif year%4==0 and year%100==0 and year%400==0:
    print("El año es bisiesto")

# Solution 4

a=int(input("Insert year: "))
if (a%4==0 and not a%100==0) or (a%4==0 and a%100==0 and a%400==0):
    print("Leap year")
else: print("Not leap year") 
