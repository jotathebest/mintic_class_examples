# List
my_list = [True, "string", 1, 3.4, False]
# print(my_list[3])
# print(my_list[4])
name = "diana"
diana = "marcela"
my_list = [name, diana, "diana"]
# print(my_list)


# Tuples
my_tuple = (True, "string", 1, 3.4, False)
# print(my_tuple[3])
# print(my_tuple[4])

# print(my_list)
my_list[0] = False
# print(my_list)

# This cannot be done
# my_tuple[0] = False

# print(my_list)
my_list.append("otro valor")
# print(my_list)

my_list = ["jose", "garcia", "garcia", "garcia", "garcia", True]
# print(my_list)
my_list.remove("garcia")
# print(my_list)


my_list = ["jose", "garcia", "delgado", "garcia", "garcia", True]
my_bool = my_list.pop()
print(my_list)
print(my_bool)

my_bool = my_list.pop(2)
print(my_list)
print(my_bool)
