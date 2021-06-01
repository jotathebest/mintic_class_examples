# default parameters


def fun(a, b, c=1, d=2):
    pass


import datetime


def func(delta_days=5):
    return datetime.datetime.now() + datetime.timedelta(days=delta_days)


# Create a function that makes a math operation to a given number. By default, it should be to calculate
# the sqrt

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
