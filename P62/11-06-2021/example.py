# my_dict = {"name": "jose", "surname": "garcia", "name": "jose-1"}
# print(my_dict)
# my_set = {True, 1, 2, 3, 4, 5, "jose", 3.4, -9}

# print(my_set)

# my_set = {1, 2, 3, 1, 2, 3, 4, 5 ,6, 1, 3}
# print(my_set)

# my_list = ["jose", "jose", "carolina", "jose", "betsy"]
# my_set = set(my_list)
# print(my_set)

x1 = {"foo", "baz", "bar"}
x2 = {"qux", "baz", "quux"}

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
print(x_diff)
x_diff = x2.difference(x1)
print(x_diff)
x_diff = x1 - x2
print(x_diff)

# symmetric difference
x_sym_diff = x1.symmetric_difference(x2)
print(x_sym_diff)

print("*" * 10)

x1 = {"foo", "bar", "qux"}
x2 = {"foo", "qux"}

print(x2.issubset(x1))
print(x1.issuperset(x2))

print("*" * 10)

x1 = {1, 2}
# error
# x1[0]

print(x1)
x1.update([3, 4, 5])
print(x1)

my_list = list(x1)
print(my_list[0])

# tuples --> inmutables, allows repeated elements
# lists --> mutables, allows repeated elements
# sets --> mutables, do not allow repeated elements
