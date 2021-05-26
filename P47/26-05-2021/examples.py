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
