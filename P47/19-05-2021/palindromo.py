# Los palíndromos son frases que se leen igual de derecha de izquierda que de
# izquierda a derecha. Por ejemplo, anita lava la tina es un palíndromo, ya que
# obviando los espacios en blanco, la frase se lee igual. Elabora un programa que diga
# si una frase es un palíndromo o no.

# Solution 1
phrase = input("Insert a phrase to analyse: ")
phrase = phrase.replace(" ", "")
original = []
new_phrase = []

for letter in phrase:
    original.append(letter)

length = len(phrase)
for index in reversed(range(0, length)):
    letter = phrase[index]
    new_phrase.append(letter)

print(original == new_phrase)

# Solution 2

phrase = input("Insert a phrase to analyse: ")
phrase = phrase.replace(" ", "")
new_phrase = phrase[::-1]
print(phrase == new_phrase)
