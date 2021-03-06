print(type(True) == type(1))

# input --> my_list = [True, "jose", 2.3, "garcia", 25, 60]
# output --> [True, "jose", 4.6, "garcia", 50, 120]

def double_list(my_list):
    for index, element in enumerate(my_list):
        # if type(element) == int or type(element) == float
        if type(element) in [int, float]:
            my_list[index] = my_list[index] * 2
    return my_list

result = double_list([True, "jose", 2.3, "garcia", 25, 60])
print(result)

# max - min

max(1, 3, 4, 5, -1)
max([1, 3, 4, 5, -1])
max((1, 3, 4, 5, -1))
max(("1", 3, 4, 5, -1))
min(("1", "3", "4", "5", "-1"))

# sorted

sorted([1, 4, 5, 1, -1, 10, -4], reverse=True)
sorted([1, 4, 5, 1, -1, 10, -4])
sorted([1, 4, 5, 1, -1, 10, -4], reverse=False)


