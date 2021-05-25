# Create a program that verifies if a parenthesis inside a phrase is properly closed
# Crea un programa que verifique si un parentésis dentro de una frase es cerrado correctamente

# print('hello')  --> True
# Estaba en el mercado (aunque no queria) mientras mi hermano se quedó durmiendo --> True
# Estaba en el mercado (aunque no queria mientras mi hermano se quedó durmiendo --> False
# (hola carambola (estas cerrando) (muy mal los parentesis --> False
# (hola carambola) (estas cerrando) (muy bien los parentesis) --> True
# (hola carambola (estas cerrando (muy bien los parentesis))) --> True

phrase = input("Inserte la frase: ")

# Solution 1
# contador = 0
# for letter in phrase:
#     if letter == "(":
#         contador += 1
#     if letter == ")":
#         contador -= 1

# print("es correcto" if contador == 0 else "es incorrecto")

# Solution 2
parentesis_abren = 0
parentesis_cierran = 0

for letter in phrase:
    if letter == "(":
        parentesis_abren +=1
    if letter == ")":
        parentesis_cierran +=1

print("es correcto" if parentesis_cierran == parentesis_abren else "es incorrecto")
