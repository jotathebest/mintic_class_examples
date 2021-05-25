# Dada una cadena de caracteres, determine cual es el caracter que mas se repite y
# cuantas veces(case insensitive)
# ejemplo: input = 'hola soy la letra mas repetida'
# output = a 5

phrase = input("Inserte una frase: ")
phrase.replace(" ", "").lower()

# {"a": 1, "b": 4, "c": 4 ...}

# hahjo
score = {}
for letter in phrase:
    if not letter in score.keys():
        score[letter] = 1
    else:
        score[letter] += 1

# iteration 1
# letter --> h
# h in [] --> False
# score[h] = 1 --> {"h": 1}

# Iteration 2
# letter --> a
# a in ["h"] --> False
# score[a] = 1 --> {"h": 1, "a": 1}

# iteration 3
# letter --> h
# h in ["h", "a"] --> True
# score["h"] += 1 --> {"h": 2, "a":1}

# {"h": 2, "a":1, "z": 4, "j": 1, "o": 1}

frequency = 0
letter = ""
for key, value in score.items():
    if value > frequency:
        letter = key
        frequency = value

# iteration1
# key, value --> h, 2
# frequency, letter --> 0, ""
# value > frequency --> 

print(f"la letra que mas se repite en la frase '{phrase}' es {letter} con {frequency}")
