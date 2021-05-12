# Challenge https://www.hackerrank.com/challenges/py-if-else/problem

n = input("Insert a number: ")

# Solution 1

if n < 1 or n > 100:
    print("not valid")
elif n % 2 != 0:
    print("Weird")
elif n >= 2 and n <= 5 and n % 2 == 0:
    print("Not Weird")
elif n >= 6 and n <= 20 and n % 2 == 0:
    print("Weird")
else:
    print("Not Weird")

# Solution 2

if n < 1 or n > 100:
    print("not valid")
elif n % 2 != 0:
    print("Weird")
elif n >= 2 and n <= 5:
    print("Not Weird")
elif n >= 6 and n <= 20:
    print("Weird")
else:
    print("Not Weird")

# Solution 3

if n < 1 or n > 100:
    print("not valid")
else:
    if n % 2 != 0:
        print("Weird")
    elif n >= 2 and n <= 5:
        print("Not Weird")
    elif n >= 6 and n <= 20:
        print("Weird")
    else:
        print("Not Weird")

# Solution 4

if n < 1 or n > 100:
    print("not valid")
if n % 2 != 0:
    print("Weird")
if n >= 2 and n <= 5 and n % 2 == 0:
    print("Not Weird")
if n >= 6 and n <= 20 and n % 2 == 0:
    print("Weird")
if n > 20 and n % 2 == 0:
    print("Not Weird")

# Solution 5

if n < 1 or n > 100:
    print("not valid")
elif n % 2 != 0:
    print("Weird")
elif n in range(2, 6):
    print("Not Weird")
elif n in range(6, 21) and n % 2 == 0:
    print("Weird")
else:
    print("Not Weird")

# Solution 6

if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and n >= 2 and n <= 5:
    print("Not Weird")
elif n % 2 == 0 and n in range(6, 21):
    print("Weird")
else:
    print("Weird")
