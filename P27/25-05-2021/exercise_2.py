# Write a Python function to find the Max of three numbers.

def get_max(number_1, number_2, number_3):
    if number_1 >= number_2 and number_1 >= number_3:
        return number_1
    if number_2 >= number_1 and number_2 >= number_3:
        return number_2
    if number_3 >= number_1 and number_3 >= number_2:
        return number_3

# number_1 = float(input("Inserte numero 1: "))
# number_2 = float(input("Inserte numero 2: "))
# number_3 = float(input("Inserte numero 3: "))

# result = get_max(number_1, number_2, number_3)
# print(f"El mayor es {result}")

# Carlos
def max_number(list):
    return max(list)

number_1 = input("Numero 1: ")
number_2 = input("\nNumero 2: ")
number_3 = input("\nNumero 3: ")
list = []
list.append(float(number_1))
list.append(float(number_2))
list.append(float(number_3))
print(max_number(list)) 

# Gidneth
def maximum(a, b, c):
    if (a >= b) and (a >= c):
        mayor = a
    elif (b >= a) and (b >= c):
        mayor = b
    else:
        mayor = c
    return mayor

a= int(input())
b = int(input())
c= int(input())
print(maximum(a,b,c))
