gender = input("Insert the gender: ")
gender = gender.upper()

if gender == 'F':
    print("correcto")
else:
    print("incorrecto")

if gender == 'F':
    print("correcto")
elif gender == 'M':
    print("correcto")
else:
    print("incorrecto")

if gender == 'F' or gender == 'M':
    print("correcto")
else:
    print("incorrecto")

if gender != 'F' and gender != 'M':
    print("incorrecto")
else:
    print("correcto")
