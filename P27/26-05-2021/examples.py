print(type(True) == type(1))

my_list = [True, "jose", 1, 4.6, "garcia"]
my_list_2 = [True, "jose", 2, 5.6, "garcia"]

def multiplicar_listas(my_list):
    for index, element in enumerate(my_list):
        if type(element) in [int, float, dict]:
            my_list[index] = my_list[index] * 2
    return my_list


print(multiplicar_listas(my_list))
print(multiplicar_listas(my_list_2))

# max - min
max(1,24,65,29)
max([1,24,65,29])
max(["1","24","65","29"])
min([1,24,65,29])

# sorted
sorted([1, 3, 5, 2, -1, 2], reverse=True)
sorted({"a": 1, "c": 2, "b": 1}, reverse=True)

# print 
print("abb", "ccc", sep="/", end="-")



