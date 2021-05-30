import random

rand_number = random.randint(1, 9)

# Write a program that asks to the user for a number, if the number matches with the rand_number
# print "you win", if not, print "You lose, the winner number is <rand_number>"

number = input("insert a number")
if number == rand_number:
    print("you win")

if number != rand_number:
    print("you lose")
