# Options --> 'F' or 'M'
gender = input("Insert your gender: ")
gender = gender.upper()

#  F != F --> False    or    F != M --> True
#  F != F --> False    and    F != M --> True
if gender != "F" and gender != "M":
    print("Your gender is not valid")
else:
    print("Your gender is valid")

# if gender == "F" or gender == "M":
#     print("The gender is valid")

# if gender != "F" and gender != "M":
#     print("The gender is not valid")

# Write a program to display "Hello" if a number entered by user is a multiple of five ,
# otherwise print "Bye".
