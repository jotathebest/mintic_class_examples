print(type(True) == type(2))

# input --> [True, "jose", "garcia", 1, 3.4, False, (), [], {"a": 1}]
# output --> [True, "jose", "garcia", 2, 6.8, False, (), [], {"a": 1}]

def double_list(my_list):
    for index, element in enumerate(my_list):
        # if type(element) == int or type(element) == float
        if type(element) in [int, float]:
            my_list[index] = my_list[index] * 2
    return my_list

result = double_list([True, "jose", "garcia", 1, 3.4, False, (), [], {"a": 1}])
print(result)

# max - min

max(1,2,3,4)
max(1,2,3,4,-1,-4)
max([1,2,3,4,-1,-4])
max((1,2,3,4,-1,-4))
max({"a": 1, "b": 2})
max({"a": 1, "b": 2}.values())
ord("a")
min({"a": 1, "b": 2, "A": 4})

# sorted
my_list = [1, 4, -1, 5, 2, -2, 1, 2]
sorted(my_list)
sorted(my_list, reverse=True)


