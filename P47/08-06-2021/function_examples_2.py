import timeit

# Return values

def foo():
    print("", end="")

# What value does result take?
result = foo()

def foo():
    print("", end="")
    pass

def foo_2(a, b, c):
    pass

# What value does result take?
result = foo()

def foo():
    print("", end="")
    return ("hello", "world")

def es_bisiesto(year):
    year = int(year)
    message = "es bisiesto"
    if not year % 4 == 0:
        message = "No es bisiesto"
    elif not year % 100 == 0:
        message = "Es bisiesto"
    elif not year % 400 == 0:
        message = "no es bisiesto"
    else:
        message = "es bisiesto"
    
    return year, message

year, message = es_bisiesto(2031)
print(year, message)
    

# Recursiveness

# 3! = 1*2*3
# 5! = 1*2*3*4*5
# 10! = 1*2*3*4*5*6*7*8*9*10
# 0! = 1
# 1! = 1

def factorial(n):
    if n in [0, 1]:
        return 1
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result


def factorial(n):
    if n in [0, 1]:
        return 1

    result = n
    for k in range(2, n):
        result *= k

    return result

my_setup = """
def factorial(n):
    if n in [0, 1]:
        return 1

    result = n
    for k in range(2, n):
        result *= k

    return result

def my_main():
    factorial(5)
"""

factorial_5 = factorial(50)
print(f"result: {factorial_5}")
execution_time = timeit.Timer(stmt="my_main()", setup=my_setup)
print(f"First approximation execution time is ", end="")
print(execution_time.timeit(5))


# N! = (N - 1)! * N
# 9! = 8! * 9 = 7! * 8 * 9

def factorial(n):
    if n in [0, 1]:
        return 1
    
    return factorial(n - 1) * n

factorial_5 = factorial(50)
print(f"result: {factorial_5}")
execution_time = timeit.Timer(stmt="my_main()", setup=my_setup)
print(f"Second approximation execution time is ", end="")
print(execution_time.timeit(5))

# write a program that returns the sum of a list of numbers
# func([1,2,3,4]) --> 10

def func(number_list):
    if len(number_list) == 0:
        return 0
    
    # [3]
    if len(number_list) == 1:
        return number_list[0]

    return func(number_list[1:]) + number_list[0]
