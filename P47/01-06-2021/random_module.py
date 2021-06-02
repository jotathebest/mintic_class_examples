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
# 1 < N < 1000

# Solution 1
def lottery():
    my_list = []
    count = 100
    while count > 0:
        number = random.randrange(1, 1000)
        my_list.append(number)
        count -= 1
    choices = random.choices(my_list, k=2)
    return choices


winners = lottery()
user_number = input("Inserte el numero ganador: ")
user_number = int(user_number)

print("ganaste" if user_number in winners else "perdiste")

# Solution 2


def lottery_generator(minimal, maximal, num_tickets):
    tickets = []
    for i in range(1, num_tickets + 1):
        tickets.append(random.randint(minimal, maximal))
    return tickets


lottery_tickets = lottery_generator(1, 1000, 100)
winner_tickets = random.choices(lottery_tickets, k=2)
user_input = int(input("Give me a number between 1 and 1000: "))
winner_flag = False

for ticket in winner_tickets:
    if user_input == ticket:
        winner_flag = True
        break

print("You are the winner!") if winner_flag else print("Sorry, try again!")

if winner_flag == True:
    print("you win")
else:
    print("you lose")

# Pick a random character from a given String

# Generate  random String of length 5.
# hint: use the string module


# Generate a random Password which meets the following conditions:
# Password length must be 10 characters long.
# It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.
