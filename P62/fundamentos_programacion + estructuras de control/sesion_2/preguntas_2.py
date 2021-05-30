import random

words = {1: "tijera", 20: "spock", 20: "papel", 4: "piedra", 5: "lagarto"}

values = words.values()
values = list(values)
print(random.choice(values))
