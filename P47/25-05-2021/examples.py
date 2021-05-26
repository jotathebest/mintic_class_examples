# def <name> (<arg_1>, <arg_2>, ... <arg_n>):
#     <algorithm>
#     [optional] return <result>

# imprimir los cuadrados del 1 al 5

def print_squares():
    for i in range(1, 6):
        print(i ** 2, end=", ")


# print_squares()
# print_squares()
# print_squares()

# imprimir los cuadrados del 1 hasta el numero que diga el usuario

def print_squares(upper_limit):
    for i in range(1, upper_limit + 1):
        print(i ** 2)

# n = int(input("Ingrese el numero 1: "))
# print_squares(n)
# m = int(input("Ingrese el numero 2: "))
# print_squares(m)
# z = int(input("Ingrese el numero 3: "))
# print_squares(z)

# imprimir los cuadrados del 1 hasta el numero que diga el usuario,
# y el resultado multiplicarlo por 3

def print_squares(upper_limit):
    result = []
    for i in range(1, upper_limit + 1):
        result.append(i ** 2)
    return result

number = 3
resultado = print_squares(number)
for element in resultado:
    print(element * 3)

