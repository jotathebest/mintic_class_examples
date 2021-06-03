# Write a Python script to concatenate following dictionaries to create a new one.

# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# iterar
for key in dic1.keys():
    print(key)

for value in dic1.values():
    print(value)

for key, value in dic1.items():
    print(key, value)


# obtener valores
my_dict = {"name": "jose", "surname": "garcia", "email": "test@test.com", "age": 30}
my_dict["name"]
my_dict.get("name-1", "la llave no existe")

# crear valores
my_dict = {}
my_dict["name"] = "jose"


# Write a Python script to check whether a given key already exists in a dictionary.

# Write a Python program to iterate over dictionaries using for loops.

# Write a Python script to generate and print a dictionary that contains a number (between 1 and n)
# in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Write a Python program to sum all the items in a dictionary.
# my_dict =  {'data1':100,'data2':-54,'data3':247}

# Write a Python program to combine two dictionary adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

# Write a Python program to print all unique values in a dictionary.
# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}

# Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
