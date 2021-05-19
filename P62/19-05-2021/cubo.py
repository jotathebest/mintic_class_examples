# Genere un programa que reciba un entero n, entre 1 y 20, y que imprima el cubo de
# los números desde 1 hasta n espaciados por un final de línea, avanzando de 1 en 1.

n = input("Insert a upper limit number: ")
n = int(n)

# Solution 1

while n >= 1:
    print(n ** 3)
    n -= 1


# Solution 2

n = input("Insert a upper limit number: ")
n = int(n)
for i in range(1, n + 1):
    print(i ** 3)


# Solution 3

n = input("Insert a upper limit number: ")
n = int(n)
result = []

while n >= 1:
    result.append(n ** 3)
    n -= 1

result.reverse()
for i in result:
    print(i)


# Solution 4

n = input("Insert a upper limit number: ")
n = int(n)

j = 20

while n >= 1:
    if n == j:
        for i in range(1, n + 1):
            print(i ** 3)
        break
    else:
        j -= 1
