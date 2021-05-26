# def <name> (<arg_1>, <arg_2>, ... <arg_n>):
#     <algorithm>
#     [optional] return <result>

# imprimir los cuadrados del 1 al 5

def print_squares():
    for i in range(1, 6):
        print(i ** 2, end=",")

# print_squares()

# imprimir los cuadrados del 1 hasta el número que decida el usuario

def print_squares(upper_limit):
    for i in range(1, upper_limit + 1):
        print(i ** 2, end=",")

# number_1 = int(input("Ingrese el numero 1: "))
# print_squares(number_1)
# number_2 = int(input("Ingrese el numero 2: "))
# print_squares(number_2)
# number_3 = int(input("Ingrese el numero 3: "))
# print_squares(number_3)

def print_squares(upper_limit):
    result = []
    for i in range(1, upper_limit + 1):
        result.append(i ** 2)
    return result

number_1 = int(input("Ingrese el numero 1: "))
squares = print_squares(number_1)
for element in squares:
    print(element, end=",")
