# Dadas dos listas, imprime el nombre junto con la edad de la persona
# Jose 29
# Diana 28
# Hacer dos scripts, uno usando for y otro usando while

people = ["Jonas", "Julio", "Mike", "Mez"]
ages = [25, 30, 31, 39, 50]

# for i in range(0, len(my_list_2)):
#    print(f"i: {i} - {my_list_1[i]} - {my_list_2[i]}")

# for num_1, num_2 in zip(my_list_1, my_list_2):
#    print(num_1 - num_2)

max_index = max(len(people), len(ages))
min_index = min(len(people), len(ages))
for i in range(0, max_index):
    if i <= min_index:
        continue
    people[i] = ""

for i in range(0, len(ages)):
    name = people[i]
    age = ages[i]
    print(f"{name} {age}")

for name, age in zip(people, ages):
    print(f"{name} {age}")
