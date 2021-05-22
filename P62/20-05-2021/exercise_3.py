# A prime number (or a prime) is a natural number greater than 1 that has no positive divisors
# other than 1 and itself. A natural number greater than 1 that is not a prime number
# is called a composite number.

# Based on this definition, if we consider the first 10 natural numbers, we can see that 2, 3, 5,
# and 7 are primes, while 1, 4, 6, 8, 9, 10 are not. In order to have a computer tell you
# if a number N is prime, you can divide that number by all natural numbers in the range [2, N ).
# If any of those divisions yields zero as a remainder, then the number is not a prime.

# Write a program to find all the primes numbers from 1 to N, where N is an integer given by the user.
# Write two scripts, one using while and other one using for

# N = 10
# 23456789
# [2, 3, 5, 7]

# Miguel

# numero = int(input("Inserte un número natural: "))
# if numero < 0:
#     print("inserte un número natural.")
# else:
#     for i in range(1, numero + 1):
#         primo = True
#         for j in range(1, i):
#             if i % j == 0 and j != i and j != 1:
#                 primo = False
#         if primo == True:
#             print(i)

# Jose
# N = 10
# 23456789
# [2, 3, 5, 7]
n = input("Inserte el numero N: ")
n = int(n)
primes = []

for number in range(2, n):  # for-number
    is_prime = True
    for divisor in range(2, number):  # for-divisor
        if number % divisor == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(number)

print(primes)

# Iteration #1 for-number
# number --> 2
# Iteration #1 for-divisor
# number --> 2 ; divisor --> Null
# is_prime --> True
# primes.append(2)

# Iteration #2 for-number
# number --> 3
# Iteration #1 for-divisor
# number --> 3 ; divisor --> 2
# number % divisor == 0 --> False
# is_prime --> True
# primes.append(3)

# Iteration #3 for-number
# number --> 4
# Iteration #1 for-divisor
# number --> 4 ; divisor --> 2
# number % divisor == 0 --> True
# is_prime --> False

# Iteration #4 for-number
# number --> 5
# Iteration #1 for-divisor
# number --> 5 ; divisor --> 2
# number % divisor == 0 --> False
# Iteration #2 for-divisor
# number --> 5 ; divisor --> 3
# number % divisor == 0 --> False
# Iteration #3 for-divisor
# number --> 5 ; divisor --> 4
# number % divisor == 0 --> False
# is_prime --> True
# primes.append(5)
