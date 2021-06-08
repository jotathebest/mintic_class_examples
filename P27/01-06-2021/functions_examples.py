# default parameters

def fun(a, b, c=1, d=2):
    pass


import datetime


def func(delta_days=5):
    return datetime.datetime.now() + datetime.timedelta(days=delta_days)


# Create a function that makes a math operation to a given number. By default, it should be to calculate
# the sqrt

import math
number = input("inserte numero: ")

def operate_number(number, default_operation="sqrt"):
    if default_operation == "sqrt":
        return math.sqrt(number)
    if default_operation == "tan":
        return math.tan(number)

def operate_number(number, default_operation=math.sqrt):
    return default_operation(number)

def sumar(number_1, number_2=1):
    return number_1 + number_2

MISC_FUNCS = {
    "tan": math.tan,
    "sqrt": math.sqrt,
    "sumar": sumar,
}

def operate_number(number, default_operation="sqrt"):
    return MISC_FUNCS[default_operation](number)


# Positional arguments


def minimum(*n):
    # print(n) # n is a tuple
    mn = n[0]
    for value in n[1:]:
        if value < mn:
            mn = value
    print(mn)


# Create a function that calculates the maximum inside a list

# variable keywords


def func(**kwargs):
    print(kwargs)

data = {"name": "jose", "surname": "garcia"}
def func(name, **kwargs):
    print(name)
