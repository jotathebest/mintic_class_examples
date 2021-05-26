# Write a Python function that takes a list and returns a new list with unique elements of the first list.
# [1, 2, 3, 4, 5, 4, 3, 7, 9]
# [1, 2, 3, 4, 5, 7, 9]


def pedir_numeros():
    length = 5
    my_list = []
    while length > 0:
        number = int(input("Inserte el número a agregar: "))
        my_list.append(number)
        length -= 1
    return my_list

def get_unique_elements(my_list):
    result = []
    for element in my_list:
        if element not in result:
            result.append(element)
    return result

# my_list = [1, 2, 3, 4, 5, 4, 3, 7, 9]
my_list = pedir_numeros()
my_list_2 = [1, 6, 8, 10, 10, 2, 1, 1]
result = get_unique_elements(my_list)
result2 = get_unique_elements(my_list_2)
print(result, result2)
