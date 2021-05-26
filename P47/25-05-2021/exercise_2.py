# Write a Python function to find the Max of three numbers.

# Jose
def get_max_number(number_1, number_2, number_3):
    if number_1 >= number_2 and number_1 >= number_3:
        return number_1
    if number_2 >= number_1 and number_2 >= number_3:
        return number_2
    if number_3 >= number_2 and number_3 >= number_1:
        return number_3

# number_1 = float(input("Inserte numero 1: "))
# number_2 = float(input("Inserte numero 2: "))
# number_3 = float(input("Inserte numero 3: "))

# result = get_max_number(number_1, number_2, number_3)
# print(result)

# Samaris
def HigherNumber(list_numbers):
    numberH = 0
    for i in list_numbers:
        if i > numberH:
            numberH = i
    print(numberH)

list_numbers = [1, 5, 3, -1, 10, 200, -400]
HigherNumber(list_numbers) 

# Camilo
def max_finder(a, b, c):
    return max(a, b, c)

number1 = int(input("Number #1: "))
number2 = int(input("Number #2: "))
number3 = int(input("Number #3: "))
print(f"The maximal number is {max_finder(number1, number2, number3)}") 
