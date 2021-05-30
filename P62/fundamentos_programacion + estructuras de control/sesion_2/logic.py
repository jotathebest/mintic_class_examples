# Logical operators
# print(3 > 3)
# print(3 >= 3)
# print(True >= False)
# print(2 != 5)
# print("jose" != "garcia")
# print("jjjj" == "j" * 4)
# print(True >= False + 1)
# print(True == "True")
# print(1 != "1")
# print(1 == "1")
# print(float(True) != 1.0)
# print(1 == 1.0)
# print(True != "jose")

# AND --> True only if all the inputs are True
# Simil *

my_bool_1 = True
my_bool_2 = True
my_bool_3 = False

# print(my_bool_1 and my_bool_2 and my_bool_3)
# print((my_bool_1 and my_bool_2) and True)
# print((my_bool_1 and my_bool_3) and "jjj" == "jjj")

# OR --> False only if all the inputs are False
# Simil +

my_bool_1 = True
my_bool_2 = True
my_bool_3 = False

# print(my_bool_3 or my_bool_1 or my_bool_2)
# print(my_bool_3 or False)
# print((my_bool_1 and my_bool_3) or my_bool_2)
# print(
#     (my_bool_3 and my_bool_1)
#     and (my_bool_2 or my_bool_1)
#     and "jjj" != "jj"
#     or my_bool_2
# )

# print(
#     (my_bool_3 and my_bool_1)
#     and (my_bool_2 or my_bool_1)
#     and ("jjj" != "jj" or my_bool_2)
# )

# Not --> Changes the output status

my_bool_1 = True
my_bool_2 = True
my_bool_3 = False

print(not (my_bool_1 and my_bool_3))
print(not True)

# Xor --> True if all the inputs are different

# print(my_bool_1 xor my_bool_2)
