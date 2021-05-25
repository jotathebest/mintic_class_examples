# Write a Python program to reverse a string
# Sample String : "1234abcd"
# Expected Output : "dcba4321"

# def <name> (<arg_1>, <arg_2>, ... <arg_n>):
#     <algorithm>
#     [optional] return <result>

def reverse_str(phrase):
    result = phrase[::-1]
    print(result)

# my_str = input("Inserte la frase: ")
# reverse_str(my_str)

# my_list = ["hola, frase 1","hola, frase 2", "hola, frase 3", "hola, frase 4"]
# for element in my_list:
#     reverse_str(element)

# Solution 2

def reverseString(chain):
    string_list = list(chain)
    return ''.join(string_list[::-1])

print(reverseString(input()))

# Solution 3

Frase = str(input("Ingrese frase: "))
def reverse(Frase):
    str = ""
    for i in Frase:
        str = i + str
    return str
print("La cadena origin : " + Frase,end="")
print("La cadena invertida usando bucle: " + reverse(Frase), end="")
