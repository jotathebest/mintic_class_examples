# Generate 3 random integers between 100 and 999 which is divisible by 5
import random

numbers = []
for i in range(1, 4):
    numero = random.randrange(0, 100, 5)
    numbers.append(numero)
print(numero)

# EJERCICIO 1
import random


def num_div_cinco():
    num1 = 0
    num2 = 0
    num3 = 0
    num1 = random.randrange(100, 999, 5)
    num2 = random.randrange(100, 999, 5)
    num3 = random.randrange(100, 999, 5)
    return (num1, num2, num3)


print(num_div_cinco())

# Random Lottery Pick. Generate 100 random lottery tickets and pick two lucky tickets from it as a winner.
# Asks to the user for a number, and print if he is a winner or not

# Pick a random character from a given String

# Generate  random String of length 5.
# hint: use the string module


# Generate a random Password which meets the following conditions:
# Password length must be 10 characters long.
# It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.
