# Conjuntos
my_bool = True
my_set = {my_bool, "string", 2, "another-string", True}
# print(my_set)

# lists
my_list = [True, 1, 3.4, "string"]
# print(my_list)
# print(my_list[2])
# print(my_list[3])

# tuples
my_tuple = (True, 1, 3.4, "string")
# print(my_tuple)
# print(my_tuple[0])

# Difference
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_list[1] = "jose"
# print(my_list)
# my_tuple[1] = "jose"

my_list = ["jose"]
my_list.append("garcia")
print(my_list)

my_list = ["jose", "garcia", "garcia", "garcia", "garcia", True]
my_list.remove("garcia")
print(my_list)

my_bool = my_list.pop()
print(my_bool)

my_name = my_list.pop(0)
print(my_name)
