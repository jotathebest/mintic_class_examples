my_set = {1, "3", True}
# print(my_set)

my_list = [1, "string", True, 3.4]

# print(my_list[3])

my_tuple = (1, "string", True, 3.4)
# print(my_tuple[1])

my_list[3] = my_list[3] * 2
# print(my_list[3])
# print(my_list)

# my_tuple[3] = my_tuple[3] * 2
# print(my_tuple[3])
# print(my_tuple)

my_list.append("another string")
# print(my_list)

my_list = my_list * 3
# print(my_list)

my_tuple = my_tuple * 3
# print(my_tuple)

# print(tuple(my_list))
# print(list(my_tuple))

# print(len(my_list))
# print(my_list[14])

print(my_list)
# my_list.remove("string")
# my_list.pop(5)
print(my_list)

sub_list = my_list[0:3]
print(sub_list)

print(my_list[5::])

my_list = [1, 2, 3, 4, 5]
print(my_list[:-3])
