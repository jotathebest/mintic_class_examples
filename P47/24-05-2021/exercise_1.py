# Create a program that verifies if a parenthesis inside a phrase is properly closed
# Crea un programa que verifique si un parentésis dentro de una frase es cerrado correctamente

# print('hello')  --> True
# Estaba en el mercado (aunque no queria) mientras mi hermano se quedó durmiendo --> True
# Estaba en el mercado (aunque no queria mientras mi hermano se quedó durmiendo --> False
# (hola carambola (estas cerrando) (muy mal los parentesis --> False
# (hola carambola) (estas cerrando) (muy bien los parentesis) --> True
# (hola carambola (estas cerrando (muy bien los parentesis))) --> True

phrase = input("inserte la frase: ")
phrase.replace(" ", "")

contador = 0
for letter in phrase:
    if letter == "(":
        contador += 1
    if letter == ")":
        contador -= 1

print("Es correcto" if contador == 0 else "es incorrecto")
