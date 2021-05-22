# Dadas dos listas, imprime el nombre junto con la edad de la persona
# Jose 29
# Diana 28
# Hacer dos scripts, uno usando for y otro usando while

people = ["Jonas", "Julio", "Mike", "Mez"]
ages = [25, 30, 31, 39]

length = len(people)

for i in range(0, length):
    name = people[i]
    age = ages[i]
    print(f"{name} {age}")
