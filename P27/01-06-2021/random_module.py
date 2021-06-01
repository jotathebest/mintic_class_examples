# Generate 3 random integers between 100 and 999 which is divisible by 5
import random
import string

# Solution 1

rand_num = [random.randrange(100, 999, 5) for i in range(1, 4)]
print(rand_num)

# Solution 2
my_numbers = []

while True:
    number = random.randrange(100, 999)
    if number % 5 == 0:
        my_numbers.append(number)
    else:
        continue
    if len(my_numbers) == 3:
        break

for i in my_numbers:
    print(f"{i}")

# Random Lottery Pick. Generate 100 random lottery tickets and pick two lucky tickets from it as a winner.
# Asks to the user for a number, and print if he is a winner or not
# 1 < n < 1000

random_numbers = []
for i in range(0, 101):
    aleatorio = random.randrange(1, 999)
    random_numbers.append(aleatorio)

random_numbers = [random.randrange(1, 999) for i in range(0, 101)]


number_winner_1 = random.choice(random_numbers)
number_winner_2 = random.choice(random_numbers)

while number_winner_2 == number_winner_1:
    number_winner_1 = random.choice(random_numbers)
    if number_winner_2 != number_winner_1:
        break

user_number = input("Escoger el numero ganador: ")
user_number = int(user_number)

if user_number == number_winner_1 or user_number == number_winner_2:
    print("ganaste")
else:
    print("perdiste")

print("ganaste" if user_number in [number_winner_1, number_winner_2] else "perdiste")


# Pick a random character from a given String

# Generate  random String of length 5.
# hint: use the string module
letters = string.ascii_letters
random_str_list = random.choices(letters, k=5)
my_str = ""
for letter in random_str_list:
    my_str = my_str + letter
print(my_str)

my_str = "".join(random_str_list)
print(my_str)

# Generate a random Password which meets the following conditions:
# Password length must be 10 characters long.
# It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.

upper_letters = random.choices(string.ascii_uppercase, k=2)
digit = random.choices(string.digits, k=1)
special_symbol = random.choices(string.punctuation, k=1)
lower_letters = random.choices(string.ascii_lowercase, k=6)
