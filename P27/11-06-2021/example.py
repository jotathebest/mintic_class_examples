# my_set = {1, 2, True, False, 3, 4.5}
# my_dict = {1: 2, 3: 4}
# print(my_set)

# my_set = {1, 1, 1, 1, 2}
# print(my_set)

# tuples --> inmutables
# lists --> mutables
# sets --> unique elements, mutables

# my_list = [1, 2, 3, 4, 5, 5, 5, 3, 1]
# my_set = set(my_list)
# print(my_set)

# my_tuple = (1, 2, 3, 4, 5, 5, 5, 3, 1)
# my_set = set(my_tuple)
# print(my_set)

# my_new_list = list(my_set)
# print(my_new_list)


x1 = {"foo", "bar", "baz"}
x2 = {"qux", "quux", "baz"}

# union

x_union = x1.union(x2)
print(x_union)
x_union = x1 | x2
print(x_union)

# intersection

x_intersection = x1.intersection(x2)
print(x_intersection)
x_intersection = x1 & x2
print(x_intersection)

# difference

x_diff = x1.difference(x2)
x_diff_2 = x2.difference(x1)
print(x_diff, x_diff_2)
x_diff = x1 - x2

# symmetric difference

x_sym = x1.symmetric_difference(x2)
print(x_sym)

x1 = {"foo", "bar", "baz"}
x2 = {"foo", "baz"}

print(x2.issubset(x1))
print(x1.issuperset(x2))

x1 = {"foo", "bar", "baz"}
print("*" * 10)
print(x1)
x1.update(["qux", "quux"])
print(x1)

my_list = list(x1)
for element in my_list:
    print(element)
