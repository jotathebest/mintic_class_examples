import math

my_number = 4
result = math.sqrt(my_number)
#print(result)

# print(math.floor(my_number))
# print(math.sqrt(my_number))
# print(math.pi, math.e)

# Create a program that calculates the hypotenuse of an line rect angle triangle
# h = raiz(x^2 + y^2)

x = 4
y = 5
h = math.sqrt(x**2 + y**2)
# print(f"The hypotenuse is {h}")

# Create a program that calculates the area of a circle using a radius given by the user
"""
radius = input("Please insert the circle's radius: ")
radius = float(radius)
area = math.pi * radius**2
print(f"The area of a circle of radius {radius} is {area}")
"""

from math import sqrt, pi, floor

print(sqrt(4), pi)

from math import sqrt as raiz_cuadrada, pi as numero_pi

print(floor(9))

# Write a Python program to convert true to 1 and false to 0
bool_1 = True
bool_1 = int(bool_1)
print(int(True), int(False))

# Write a program that takes a positive float and returns the nearest 
# smallest integer of the cube of the number.

# math.floor
# x ** 3

x = input("Insert a number: ")
x = float(x)
smallest = math.floor(x ** 3)
print(f"the nearest smallest integer is {smallest}")