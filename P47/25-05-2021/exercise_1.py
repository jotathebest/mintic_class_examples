# Write a Python program to reverse a string
# Sample String : "1234abcd"
# Expected Output : "dcba4321"

# def <name> (<arg_1>, <arg_2>, ... <arg_n>):
#     <algorithm>
#     [optional] return <result>

# Jose
# def reverse_string(phrase):
#     return phrase[::-1]

# phrase_1 = input("Ingrese la frase: ")
# result = reverse_string(phrase_1)
# print(result)

# Frederick
def Reverse (Str):
    for i in reversed(range(0, len(Str))):
        print(Str[i], end="")

# String = input()
# Reverse(String)

# Frederick 2
def Reverse (Str):
    result = ""
    for i in reversed(range(0, len(Str))):
        result += Str[i]
    return result

# String = input()
# result = Reverse(String)
# print(result)

# Aldo
lista = input()
def invertirString(lista):
    lista = ''.join(reversed(lista))
    return lista

print(invertirString(lista))
