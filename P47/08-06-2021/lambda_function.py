# reference
# MLA, 8.ª edición (Modern Language Assoc.)
# Romano, Fabrizio, et al. Python: Journey From Novice to Expert. Packt Publishing, 2016.

# APA, 7.ª edición (American Psychological Assoc.)
# Romano, F., Phillips, D., & Hattem, R. van. (2016). Python: Journey From Novice to Expert. Packt Publishing.

#  example 1: adder
 
def adder(a, b):
    return a + b
    
# is equivalent to:

adder_lambda = lambda a, b: a + b

# example 2: to uppercase
def to_upper(s):
    return s.upper()

# is equivalent to:

to_upper_lambda = lambda s: s.upper()

# Exercise: Transform to lambda type the below functions

def is_multiple_of_five(n):
    return not n % 5

def get_multiples_of_five(n):
    return list( filter(is_multiple_of_five, range(n)))

print(get_multiples_of_five(50))

#  Write a Python program to filter a list of integers using Lambda that returns the even numbers

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
