# Write a Python script to concatenate following dictionaries to create a new one.

# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

my_dict = {"name": "jose", "surname": "garcia", "email": "test@test.com", "age": 30}
print(my_dict.get("name-1", None))
print(my_dict["name"])

# iterar
for key in my_dict.keys():
    print(key)

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(key, value)

# acceder a valores
my_dict["name"]
var = my_dict.get("name-1", False)

# Crear valores
my_dict["name"] = "jose nuevo creado"

# Solution Miguel
def unificar(dic1, dic2, dic3):
    llaves1 = dic1.keys()
    valores1 = dic1.values()
    llaves2 = dic2.keys()
    valores2 = dic2.values()
    llaves3 = dic3.keys()
    valores3 = dic3.values()
    dicfinal = {}
    for i, j in zip(llaves1, valores1):
        dicfinal[i] = j
    for i, j in zip(llaves2, valores2):
        dicfinal[i] = j
    for i, j in zip(llaves3, valores3):
        dicfinal[i] = j
    return dicfinal


diccionario1 = {1: 10, 2: 20}
diccionario2 = {3: 30, 4: 40}
diccionario3 = {5: 50, 6: 60}
print(unificar(diccionario1, diccionario2, diccionario3))

# Solution Jefferson

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4 = {}
for key, value in dic1.items():
    dic4[key] = value
for key, value in dic2.items():
    dic4[key] = value
for key, value in dic3.items():
    dic4[key] = value
print(dic4)

# Solution Camila


def crear_diccionario():
    dic1 = {1: 10, 2: 20}
    dic2 = {3: 30, 4: 40}
    dic3 = {5: 50, 6: 60}
    dict = dic1
    for key, value in dic2.items():
        dict[key] = value
    for key, value in dic3.items():
        dict[key] = value
    return dict


print(crear_diccionario())

# Solution Adrian
dic = {}
for i in dic1, dic2, dic3:
    for key, value in i.items():
        dic[key] = value

print(dic)

# Solution Jose

my_dict = {}
for element in [dic1, dic2, dic3]:
    my_dict.update(element)

print(my_dict)

my_dict = {**dic1, **dic2, **dic3, **dic4}
print(my_dict)

# Write a Python script to check whether a given key already exists in a dictionary.

# Write a Python program to iterate over dictionaries using for loops.

# Write a Python script to generate and print a dictionary that contains a number (between 1 and n)
# in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

list = [1, 2, 3, 4, 5]
num = {}
for x in list:
    num[x] = x * x
print(num)


def diccionario_cuadrado(n: int):
    diccionario = {}
    for i in range(1, n + 1):
        diccionario[i] = i ** 2
        print(diccionario)


n = int(input("Ingrese un n??mero: "))
diccionario_cuadrado(n)


# Write a Python program to sum all the items in a dictionary.
# my_dict =  {'data1':100,'data2':-54,'data3':247}

# Write a Python program to combine two dictionary adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

d1 = {"a": 100, "b": 200, "c": 300}
d2 = {"a": 300, "b": 200, "d": 400}

result = {}

for key, value in d1.items():
    if key not in d2.keys():
        result[key] = d2[key]
    else:
        result[key] = value + d2[key]

for key, value in d2.items():
    if key not in result.keys():
        result[key] = value

from collections import Counter

result = Counter(d1) + Counter(d2)

# Write a Python program to print all unique values in a dictionary.
# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}

# Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
