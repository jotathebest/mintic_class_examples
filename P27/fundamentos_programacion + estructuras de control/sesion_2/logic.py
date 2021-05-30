# Logic basic
my_number_1 = 2
my_number_2 = 3
# print(2 == 3)
# print(2 != 3)
# print(my_number_1 > my_number_2)
# print(2 >= 2)
# print(3 <= 3)
# print("jose" == "garcia")
# print("jose" == "jose")
# print(1 == 1.0)
# print(True == False)
# print(True >= False)
# print(True >= False + 1)
# print(True > False + 1)
# print("jjjjj" == "j" * 5)

# And OR

# And para que de True TODAS deben ser TRUE
my_bool_1 = True
my_bool_2 = True
my_bool_3 = False
# print(my_bool_1 and my_bool_2 and my_bool_3)
# print(my_bool_1 and my_bool_2 >= 0)
# print(my_bool_1 and my_bool_3 and ("jose" != "jose"))

# OR para que de FALSE TODAS deben ser FALSE
my_bool_1 = True
my_bool_2 = True
my_bool_3 = False
# print(my_bool_1 or my_bool_3)
# print(my_bool_3 or False)
print(my_bool_1 and my_bool_3 or my_bool_2)
print(my_bool_1 and my_bool_2 or ("jose" == "jose") and (my_bool_3 or my_bool_1))
