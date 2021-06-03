# Generate 3 random integers between 100 and 999 which is divisible by 5

import random
import string


def create_random():
    number_1 = random.randrange(100, 999, 5)
    number_2 = random.randrange(100, 999, 5)
    number_3 = random.randrange(100, 999, 5)
    return (number_1, number_2, number_3)


number_1, number_2, number_3 = create_random()
print(number_1, number_2, number_3)


# Random Lottery Pick. Generate 100 random lottery tickets and pick two lucky tickets from it as a winner.
# Asks to the user for a number, and print if he is a winner or not
# 1 < N < 1000


def lotto():
    bolsa = []
    ganadores = []
    while len(bolsa) <= 99:
        numero = random.randrange(1, 1001)
        bolsa.append(numero)
    ganadores = random.choices(bolsa, k=2)

    while ganadores[0] == ganadores[1]:
        ganadores = random.choices(bolsa, k=2)

    print(ganadores)

    eleccion = int(input("Escoja un numero del 1 al 1000: "))
    if eleccion in (ganadores):
        return "Ganaste"
    else:
        msg = f"Los numeros ganadores eran: {ganadores}"
    return msg


lotto()


# Pick a random character from a given String

# Generate random String of length 5.
# hint: use the string module

letters = string.ascii_letters
random_letters = random.choices(letters, k=5)

my_str = ""
for letter in random_letters:
    my_str = my_str + letter

print(my_str)

my_str = "".join(random_letters)
print(my_str)

# Generate a random Password which meets the following conditions:
# Password length must be 10 characters long.
# It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.

# string.punctuation
# string.ascii_uppercase
# string.digits

# Solution 1
upper_list = random.choices(string.ascii_uppercase, k=2)
digit_list = random.choices(string.digits, k=1)
symbol_list = random.choices(string.punctuation, k=1)
letters_list = random.choices(string.ascii_letters, k=6)

password = "".join(upper_list)
password = password + "".join(digit_list)
password = password + "".join(symbol_list)
password = password + "".join(letters_list)

password_list = list(password)
random.shuffle(password_list)
password = "".join(password_list)


# Solution 2
upper_list = random.choices(string.ascii_uppercase, k=2)
digit_list = random.choices(string.digits, k=1)
symbol_list = random.choices(string.punctuation, k=1)
letters_list = random.choices(string.ascii_letters, k=6)

password_list = upper_list + digit_list + symbol_list + letters_list
password = random.sample(password_list, k=10)
password = "".join(password)
