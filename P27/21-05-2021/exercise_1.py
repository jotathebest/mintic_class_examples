# Dada una cadena de caracteres, determine cual es el caracter que mas se repite y
# cuantas veces(case insensitive): ejemplo: input = 'hola soy la letra mas repetida'
# output = a 5

# {"a": 5, "b": 4, "c": 0}
# max(my_dict.values())
# for key, value in my_dict.items():
#    print(key, value)

phrase = input("Inserte la frase: ")
phrase = phrase.replace(" ", "").lower()
letters = {}

for letter in phrase:
    if letter in list(letters.keys()):
        letters[letter] += 1
    else:
        letters[letter] = 1

# josegarciadelgado

# iteration 1
# letter --> j
# letters.keys() --> []
# j in [] --> False
# letters --> {"j": 1}

# iteration 2
# letter --> o
# letters.keys() --> ["j"]
# o in ["j"] --> False
# letters --> {"j": 1, "o": 1}

# iteration m
# letter --> a
# letter.keys() --> ["j", "o", "s", "e", "g", "a", "r", "c", "i"]
# a in ["j", "o", "s", "e", "g", "a", "r", "c", "i"] --> True
# letter["a"] += 1 --> 2
# letters --> {"j": 1, "o": 1 ... "a": 2}

# {'j': 1, 'o': 2, 's': 1, 'e': 2, ' ': 2, 'g': 2, 'a': 3, 'r': 1, 'c': 1, 'i': 1, 'd': 2, 'l': 1}

key_max = ""
value_max = 0
for key, value in letters.items():
    if value > value_max:
        key_max = key
        value_max = value

print(f"la letra que mas se repite es {key_max} con {value_max}")


# Edwin

my_str = input('Ingrese una frase\n')
letters = []
count_letters = {}

for i in my_str:
    if i in letters:
        continue
    else:
        total = my_str.count(i)
        count_letters[i] = total
        letters.append(i)

fl = max(count_letters, key = count_letters.get) 

print(f'La letra que más se repite es la {fl}, {count_letters[fl]} veces.') 
