number = input("Insert a number: ")
number = float(number)

if number == 0:
    print("Es cero")
elif number < 0:
    print("Es negativo")
elif number > 0:
    print("Es positivo")
else:
    print("Error")

# gender --> F , M ; gender cannot be empty
# email ---> cannot be empty
# Write a program that prints "invalido" if the gender is not F, M or if the email or the
# gender is empty, else prints "valido"
# The email must contains '@'
