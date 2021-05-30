import random

rand_number = random.randint(1, 9)


# Write a program that asks to the user to insert a number. If the number inserte is equal
# to the random seed, print "You win" else print "You lose, the winner number is <number>"

number = input("Número ")

if not number.lstrip("-").isdigit():
    print("No es un número")

else:
    number = float(number)
    rand_number = random.randint(1, 9)
    if rand_number == number:
        print("Win")
    else:
        print("Lose")
        print("Era", rand_number)
