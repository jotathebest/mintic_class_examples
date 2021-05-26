# Write a Python function to find the Max of three numbers.

# def <name> (<arg_1>, <arg_2>, ... <arg_n>):
#     <algorithm>
#     [optional] return <result>

# Jose
def get_max_number(number_1, number_2, number_3):
    if number_1 >= number_2 and number_1 >= number_3:
        return number_1
    if number_2 >= number_1 and number_2 >= number_3:
        return number_2
    if number_3 >= number_1 and number_3 >= number_2:
        return number_3

# number_1 = float(input("Ingrese el número 1: "))
# number_2 = float(input("Ingrese el número 2: "))
# number_3 = float(input("Ingrese el número 3: "))

# result = get_max_number(number_1, number_2, number_3)
# print(f"El número mayor es {result}")

# Roger

def Max_Number(a, b, c):
    Max_Num= max(a,b,c)
    print(Max_Num)

A= float(input("Number 1:"))
B= float(input("Number 2:"))
C= float(input("Number 3:"))

Max_Number(A, B, C)

# Juan
def numero_mayor(a,b,c):
    return f"El numero mayor es {max(a,b,c)}" 

a, b, c = input("Ingrese 3 numeros separados: ").split()
print(numero_mayor(a,b,c))
