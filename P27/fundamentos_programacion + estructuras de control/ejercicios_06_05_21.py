# import math

# my_number = 4
# result = math.sqrt(my_number)
# print(f"the square root of {my_number} is: {result}")

# Calculate y= x^2+2cosx

# x = 2
# y = x ** 2 + 2 * math.cos(x)
# print(f"result is {y}")

# # Calculate z = x * y + 2tanh(x+y)

# x=int(input("Ingrese el valor de x: "))
# y=int(input("Ingrese el valor de y: "))

# z=x*y+2*math.tan(x+y)
# print(f"resultat is {z}")

# import math
# math.sqrt(4)

from math import sqrt as sq
print(sq(4))

#  Write a Python program to print without newline or space

print("hola", end="")

# Write a Python program to calculate the hypotenuse of a right angled triangle
from math import sqrt

b=2
c=2
a=sqrt(b**2 + c**2)
print(a)

# Write a Python program to calculate body mass index
# Fórmula: peso (kg) / [estatura (m)]2

# Ingrese la estatura en metros
altura = float(input('Ingrese su altura en metros: \n'))
# Ingrese el peso en KG
peso = float(input('Ingrese su peso en kilogramos: \n'))
# Hallar IMC
imc = peso / (altura**2)
# Mostramos el valor
print(f'El indice de masa corporal es de {round(imc, 2)}')


