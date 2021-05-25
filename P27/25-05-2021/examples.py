# def <name> (<arg_1>, <arg_2>, ... <arg_n>):
#     <algorithm>
#     [optional] return <result>

# imprimir los cuadrados del 1 al 5

def print_squares():
    for i in range(1, 6):
        print(i ** 2, end=", ")

# print_squares()

# imprimir los cuadrados del 1 hasta el valor que diga el usuario

def print_squares(upper_limit):
    for i in range(1, upper_limit + 1):
        print(i ** 2, end=", ")

n = input("Ingrese limite superior: ")
n = int(n)
print_squares(n)
m = input("\nIngrese limite superior: ")
m = int(m)
print_squares(m)

def print_squares(upper_limit):
    result = []
    for i in range(1, upper_limit + 1):
        result.append(i ** 2)
    return result

z = input("\nIngrese limite superior: ")
z = int(z)
result = print_squares(z)
print(result)
