# A prime number (or a prime) is a natural number greater than 1 that has no positive divisors
# other than 1 and itself. A natural number greater than 1 that is not a prime number
# is called a composite number.

# Based on this definition, if we consider the first 10 natural numbers, we can see that 2, 3, 5,
# and 7 are primes, while 1, 4, 6, 8, 9, 10 are not. In order to have a computer tell you
# if a number N is prime, you can divide that number by all natural numbers in the range [2, N).
# If any of those divisions yields zero as a remainder, then the number is not a prime.

# Write a program to find all the primes numbers from 1 to N, where N is an integer given by the user.
# Write two scripts, one using while and other one using for

# N = 10
# 2, 3, 5, 7

n = int(input("Inserte el número N hasta donde buscaré: "))
primes = []

for index_1 in range(2, n):
    is_prime = True
    for index_2 in range(2, index_1):
        if index_1 % index_2 == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(index_1)

print(primes)

# N = 10
# Iteration 1
# index_1 --> 2 ; index_2 -->2
# 2 --> is_prime

# Iteration 2 (index_1)
# index_1 --> 3
# Iteration 1 (index_2)
# index_1 --> 3; index_2 --> 2
# index_1 % index_2 == 0 --> False
# is_prime --> True ; 3 --> es primo

# Iteration 3 (index_1)
# index_1 --> 4
# Iteration 1 (index_2)
# index_1 --> 4; index_2 --> 2
# index_1 % index_2 == 0 --> True
# is_prime = False; 4 --> no es primo

# Iteration 4 (index_1)
# index_1 --> 5
# Iteration 1 (index_2)
# index_1 --> 5; index_2 --> 2
# index_1 % index_2 == 0 --> False
# Iteration 2 (index_2)
# index_1 --> 5; index_2 --> 3
# index_1 % index_2 == 0 --> False
# Iteration 3 (index_2)
# index_1 --> 5; index_2 --> 4
# index_1 % index_2 == 0 --> False
# is_prime = True; 5 --> es primo
