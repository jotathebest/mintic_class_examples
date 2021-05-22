# Imprimir las siguientes figuras usando for y while

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

# for i in reversed(range(1, 7)):
#     print("*" * i)

# for i in range(2, 7):
#     print("*" * i)

i = 6
while i > 0:
    print("*" * i)
    i -= 1

i = 2
while i <= 6:
    print("*" * i)
    i += 1
