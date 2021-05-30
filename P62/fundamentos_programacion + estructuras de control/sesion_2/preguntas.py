# Si yo tengo un diccionario con piedra, papel o tijera, ¿Cómo escojo un elemento de manera
# aleatoria
import random

words = {"word-1": "tijera", "word-2": "piedra", "word-3": "papel"}

values = words.values()
values = list(values)
# print(random.choice(values))

keys = words.keys()
keys = list(keys)
key = random.choice(keys)
print(words[key])
