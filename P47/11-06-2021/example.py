# my_dict = {"name": "jose", "surname": "garcia"}
# my_set = {True, 1, "name", 2, 3.4, 2, 5, 1}
# print(my_set)

# my_set = set([1, 2, 3, 4, 5])
# print(my_set)

# my_set = set((1, 2, 3, 4, 5))
# print(my_set)

# my_set = set([1, 2, 3, 4, 5, 5, 5, 5, 1, 3])
# print(my_set)

# my_new_list = list(my_set)
# print(my_new_list)

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

# symetric difference
x_sym_diff = x1.symmetric_difference(x2)
print(x_sym_diff)
x_sym_diff = x1 ^ x2

print("*" * 10)

x1 = {"foo", "bar", "qux"}
x2 = {"bar", "qux"}

print(x2.issubset(x1))
print(x1.issuperset(x2))

my_list = ["jose", "jose", "jose", "carolina"]
my_set = set(my_list)
my_new_list = list(my_set)
for element in my_new_list:
    print(element)

# error
# my_set[0]

x1 = {1, 2, 3}
print(x1)
x1.update([4, 5])
print(x1)

# tuples --> inmutables
# lists --> mutables
# sets --> mutables, unique elements

