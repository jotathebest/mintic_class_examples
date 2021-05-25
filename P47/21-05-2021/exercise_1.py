# Dada una cadena de caracteres, determine cual es el caracter que mas se repite y
# cuantas veces(case insensitive): ejemplo: input = 'hola soy la letra mas repetida'
# output = a 5

phrase = input("Inserte la frase a analizar: ")
phrase.replace(" ", "").lower()

# {"a": 1, "b": 10, "c": 1 ...}
score = {}

for letter in phrase:
    if not letter in list(score.keys()):
        score[letter] = 1
    else:
        score[letter] += 1

# holaatodos
# iteration 1
# letter --> h
# list(score.keys()) --> []
# h in [] --> False
# score[h] = 1 --> {"h": 1}

# iteration 2
# letter --> o
# list(score.keys()) --> ["h"]
# o in ["h"] --> False
# score[o] = 1 --> {"h": 1, "o": 1}

# iteration 3
# letter --> l
# list(score.keys()) --> ["h", "o"]
# l in ["h", "o"] --> False
# score[o] = 1 --> {"h": 1, "o": 1, "l": 1}

# iteration 3
# letter --> a
# list(score.keys()) --> ["h", "o", "l"]
# a in ["h", "o", "l"] --> False
# score[a] = 1 --> {"h": 1, "o": 1, "l": 1, "a": 1}

# Iteration 4
# letter --> 1
# list(score.keys()) --> ["h", "o", "l", "a"]
# a in [h", "o", "l", "a"] --> True
# score[1] += 1 --> {"h": 1, "o": 1, "l": 1, "a": 2}

# score --> {"h": 1, "o": 1, "l": 1, "a": 2}

letter = ""
frequency = 0
for key, value in score.items():
    if value > frequency:
        letter = key
        frequency = value

print(f"en la frase '{phrase}' la letra que mas se repite es la {letter} con {frequency} repeticiones")
