# Write a Python function that takes a list and returns a new list with unique elements of the first list.
# [1, 2, 3, 4, 5, 4, 3, 7, 9]
# [1, 2, 3, 4, 5, 7, 9]

def get_unique_elements(my_list):
    result = []
    for element in my_list:
        if element not in result:
            result.append(element)
    return result

my_list = [1, 2, 3, 4, 5, 4, 3, 7, 9]
result = get_unique_elements(my_list)
print(result)

def get_unique_elements(my_list):
    return list(set(my_list))

result = get_unique_elements(my_list)
print(result)
