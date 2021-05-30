number = input("Qué número? ")

# Forma 1
if not number.startswith("-"):
    if not number.isdigit():
        print("Esto no es un numero")
else:
    number = number.lstrip("-")

if not number.isdigit():
    print("Esto no es un numero")

# Forma 2
# if not number.lstrip("-").isdigit():
#     print("Esto no es un número")

else:
    number = float(number)

    # if <condition>:

    if number == 0:
        print("Es cero")

    if number > 0:
        print("Es positivo")

    if number < 0:
        print("Es negativo")

# if number > 0:
#     print("Es positivo")
# else:
#     print("Es negativo")
