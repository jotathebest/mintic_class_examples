# Dadas dos listas, imprime el nombre junto con la edad de la persona
# Jose 29
# Diana 28
# Hacer dos scripts, uno usando for y otro usando while

people = ["Jonas", "Julio", "Mike", "Mez"]
ages = [25, 30, 31, 39, 40, 60]
emails = ["1@t.com", "2@t.com", "3@t.com", "4@t.com","5@t.com"]

length = len(people)

# for i in range(0, length):
#     name = people[i]
#     age = ages[i]
#     print(f"{name} {age}")

# index = 0
# while index < length:
#     name = people[index]
#     age = ages[index]
#     print(f"{name} {age}")
#     index += 1

for name, age, email in zip(people, ages, emails):
    print(f"{name} {age} {email}")
