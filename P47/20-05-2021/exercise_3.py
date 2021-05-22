# A prime number (or a prime) is a natural number greater than 1 that has no positive divisors
# other than 1 and itself. A natural number greater than 1 that is not a prime number
# is called a composite number.

# Based on this definition, if we consider the first 10 natural numbers, we can see that 2, 3, 5,
# and 7 are primes, while 1, 4, 6, 8, 9, 10 are not. In order to have a computer tell you
# if a number N is prime, you can divide that number by all natural numbers in the range [2, N ).
# If any of those divisions yields zero as a remainder, then the number is not a prime.

# Write a program to find all the primes numbers from 1 to N, where N is an integer given by the user.
# Write two scripts, one using while and other one using for

# N --> usuario
# N = 8
# 234567
# [2, 3, 5, 7]

n = input("Ingrese el número N: ")
n = int(n)

primes = []

for i in range(2, n):  # for-1
    is_prime = True
    for divisor in range(2, i):  # for-2
        if i % divisor == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)

print(primes)

# Iteration #1 for-1
# i --> 2
# Iteration #1 for-2
# i --> 2; divisor --> N/A --> El iterador no hace nada
# is_prime --> True
# primes.append(2)

# Iteration #2 for-1
# i --> 3
# Iteration #1 for-2
# i --> 3; divisor --> 2
# i % divisor == 0 --> False
# is_prime --> True
# primes.append(3)

# Iteration #3 for-1
# i --> 4
# Iteration #1 for-2
# i --> 4; divisor --> 2
# i % divisor == 0 --> True
# is_prime --> False

# Iteration #4 for-1
# i --> 5
# Iteration #1 for-2
# i --> 5; divisor --> 2
# i % divisor == 0 --> False
# is_prime --> True
# Iteration #2 for-2
# i --> 5; divisor --> 3
# i % divisor == 0 --> False
# Iteration #3 for-2
# i --> 5; divisor --> 4
# i % divisor == 0 --> False
# is_prime --> True
# primes.append(5)
