# default parameters


def fun(a, b, c=1, d=2):
    pass


import datetime
from io import DEFAULT_BUFFER_SIZE


def func(delta_days=5):
    return datetime.datetime.now() + datetime.timedelta(days=delta_days)


# Create a function that makes a math operation to a given number. By default, it should be to calculate
# the sqrt

import math

def apply_operation(number, default_operation="sqrt"):
    if default_operation == "sqrt":
        return math.sqrt(number)


def apply_operation(number, default_operation="sqrt"):
    if default_operation == "sqrt":
        return math.sqrt(number)
    if default_operation == "tan":
        return math.tan(number)
    if default_operation == "cos":
        return math.cos(number)

def apply_operation(number, default_operation=math.sqrt):
    return default_operation(number)

def sumar(number_1, number_2=4):
    return number_1 + number_2

MISC_FUNC = {
    "sqrt": math.sqrt,
    "tan": math.tan,
    "sin": math.sin,
    "suma": sumar
}

def apply_operation(number, default_operation="sqrt"):
    # operation = MISC_FUNC[default_operation]
    operation = MISC_FUNC.get(default_operation, None)
    if operation is not None:
        return operation(number)
    else:
        print("invalid")
        return None

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

# create a function that follows this structure:

# fun(<operation_math>, <number>):
#     return operation_math(number)


def fun(math_operation, number):
    return math_operation(number)

data = {"math_operation": math.sqrt, "number": 4}

fun(**data)

def fun(math_operation, number, **data):
    return math_operation(number)

data = {"math_operation": math.sqrt, "number": 4, "number-2": 45}

fun(**data)
