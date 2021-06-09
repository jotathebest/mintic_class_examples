import timeit

# Return values

def foo():
    print("", end="")

# What value does result take?
result = foo()

def foo():
    print("", end="")
    pass

def my_func(a, b, c):
    pass

# What value does result take?
result = foo()

def foo():
    print("", end="")
    return ("hello", "world")

# Recursiveness

# 6! = 1*2*3*4*5*6
# 3! = 1*2*3
# 0! = 1
# 1! = 1


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

factorial_5 = factorial(5)
print(f"result: {factorial_5}")
execution_time = timeit.Timer(stmt="my_main()", setup=my_setup)
print(f"First approximation execution time is ", end="")
print(execution_time.timeit(5))


# N! = (N - 1)! * N
def factorial(n):
    if n in [0, 1]:
        return 1
    
    return factorial(n - 1) * n

factorial_5 = factorial(5)
print(f"result: {factorial_5}")
execution_time = timeit.Timer(stmt="my_main()", setup=my_setup)
print(f"Second approximation execution time is ", end="")
print(execution_time.timeit(5))

# write a python to calculate the sum of a number list

# sumar([1,2,3,4,5]) --> 15

def sumar(number_list):
    if len(number_list) == 0:
        return 0
    elif len(number_list) == 1:
        return number_list[0]
    else:
        return sumar(number_list[1:]) + number_list[0]
