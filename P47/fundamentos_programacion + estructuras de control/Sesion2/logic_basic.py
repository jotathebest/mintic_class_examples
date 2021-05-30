# logic basic
# print(3 >= 3)
# print(3 > 3)
# print(3 != 3)
# print("jose" == "garcia")
# print("jose" == "jose")
# print(3 * 8 == 6 * 4)
# print("jjjjj" == "j" * 5)
# print(True > False)
# print(True > False + 1)
# print(True >= False + 1)
# print(True == 1.0)
# print(True != "jose")
# print(1 == "1")
# print(True == "True")

# AND --> True only if all the inputs are True
# Simil de multiplicar
my_bool_1 = True
my_bool_2 = True
my_bool_3 = False

# print(my_bool_1 and my_bool_2 and my_bool_3)
# print(my_bool_1 and "jj" != "j" and my_bool_3)
# print(my_bool_1 and "jj" != "j" and my_bool_2)
# print((my_bool_1 and my_bool_3) and (my_bool_1 and my_bool_2))

# OR --> False only if all the inputs are False
# Simil de sumar
my_bool_1 = True
my_bool_2 = True
my_bool_3 = False

# print(my_bool_1 or my_bool_3)
# print(False or my_bool_3)
# print(my_bool_1 and my_bool_2 or my_bool_3)
# print((my_bool_3 and my_bool_1) and (my_bool_3 or my_bool_1) or "jj" == "jj")

# Not --> Changes the logic state
print(not True)
print(not False)
print(not ((my_bool_3 and my_bool_1) and (my_bool_3 or my_bool_1) or "jj" == "jj"))
