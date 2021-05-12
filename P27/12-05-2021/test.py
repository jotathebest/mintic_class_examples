"""
1. si n es impar, imprimir "weird"
2. si n es par, y esta en el rango de 2 a 5,
incluyendo 2 y 5 [2, 5], imprimir "not weird"
3. si n es par, y esta en el rango de 6 a 20,
incluyendo 6 y 20, imprimir "Weird"
4. si n es par y es mayor a 20, imprimir
"Not Weird"
"""

n = input("Insert a number: ")
n = float(n)

if n < 1 or n > 100:
    print("Not valid")
else:
    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and n >= 2 and n <= 5:
        print("Not Weird")
    elif n % 2 == 0 and n in range(6, 21):
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")
    else:
        print("Not Weird")

