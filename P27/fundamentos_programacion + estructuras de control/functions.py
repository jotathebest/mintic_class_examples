import math


def find_sqrt(my_number):
    result = math.sqrt(my_number)
    print(f"The square root of {my_number} is: {result}")
    print("The square root of " + my_number + "is: " + result)


def sume_numbers(my_number_1, my_number_2):
    result = my_number_1 + my_number_2
    print(f"The sum of {my_number_1} + {my_number_2} is {result}")


my_number = 4
find_sqrt(my_number)

sume_numbers(5, 9)
# Program a function that receives as argument an angle and finds the tan of that angle
