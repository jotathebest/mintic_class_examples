# Write a Python program to reverse a string
# Sample String : "1234abcd"
# Expected Output : "dcba4321"

# def <name> (<arg_1>, <arg_2>, ... <arg_n>):
#     <algorithm>
#     [optional] return <result>

# Jose
# def reverse_string(phrase):
#     return phrase[::-1]

# phrase = input("Ingrese la frase: ")
# result = reverse_string(phrase)
# print(result)

# Miguel
def reversa(texto):
    texto2 = ""
    for i in reversed(texto):
        texto2 = texto2 + i
    print(texto2)

frase = input("Inserte una frase: ")
reversa(frase) 
