import timeit

# Return values

def foo():
    print("", end="")

# What value does result take?
result = foo()

def foo():
    print("", end="")
    pass

def foo2(a, b, c, d):
    pass

# What value does result take?
result = foo()

def foo():
    print("", end="")
    return ("hello", "world")

# Recursiveness

# 3! = 1*2*3
# 4! = 1*2*3*4
# 10! = 1*2*3*4*5*6*7*8*9*10
# 0! = 1
# 1! = 1

def factorial(n):
    if n in [0, 1]:
        return 1

    result = n
    for k in range(2, n):
        result = result * k

    return result

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
    
#     result = 1
#     for i in range(2, n + 1):
#         result = result * i
#     return result

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

factorial_5 = factorial(5000)
# print(f"result: {factorial_5}")
execution_time = timeit.Timer(stmt="my_main()", setup=my_setup)
print(f"First approximation execution time is ", end="")
print(execution_time.timeit(5))

# N! = (N-1)! * N
# 3! = 2! * 3 = 1 * 2 * 3

def factorial(n):
    if n in [0, 1]:
        return 1
    
    return factorial(n - 1) * n

factorial_5 = factorial(5000)
# print(f"result: {factorial_5}")
execution_time = timeit.Timer(stmt="my_main()", setup=my_setup)
print(f"Second approximation execution time is ", end="")
print(execution_time.timeit(5))
