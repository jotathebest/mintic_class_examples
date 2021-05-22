# Imprimir las siguientes figuras usando while y for

# Figura 1

# ******
# *****
# ****
# ***
# **
# *

# Figura 2

# ******
# *****
# ****
# ***
# **
# *
# **
# ***
# ****
# *****
# ******

# Angie
# n = input()
# n = int(n)
# figure = []

# for i in range(1, n + 1):
#     while n >= 1:
#         figure.append("*" * n)
#         n = n - 1

# for j in figure:
#     print(j)

# figure.reverse()
# for g in figure:
#     print(g)

# Camilo

# n = 6
# print("Figura #1:")
# for i in reversed(range(1, n + 1)):
#     print("*" * i)

# print("\nFigura #2:")
# for i in reversed(range(1, n + 1)):
#     if i != 1:
#         print("*" * i)
#     else:
#         break

# for i in range(1, n + 1):
#     print("*" * i)

# Jose
n = input()
n = int(n)  # n = 6
for i in reversed(range(1, n)):
    print("*" * i)
for i in range(2, n):
    print("*" * i)

# *****
# ****
# ***
# **
# *
# *
# **
# ***
# ****
# *****
