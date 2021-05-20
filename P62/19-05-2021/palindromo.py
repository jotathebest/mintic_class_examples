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


# Solution 3

is_valid = True
aux = len(phrase) - 1
max_index = len(phrase)
for i in range(0, max_index):
    if phrase[i] != phrase[aux]:
        is_valid = False
    aux -= 1

# Solution 4

inp = 'dabale arroz a la zorra el abad'.replace(" ","")
arr1 = list(inp)
arr1.reverse()
rev = ''.join(arr1)
print(True if inp == rev else False) 

# Solution 5

phrase = input("Inserte la frase: ")
phrase = phrase.replace(" ", "")
phrase = phrase.lower()


is_valid = True
max_index = len(phrase) - 1
number_of_elements = len(phrase)


for i in range(0, number_of_elements):
    if phrase[i] != phrase[max_index]:
        is_valid = False
        break
    max_index -= 1

print(
    f"la frase: {phrase} es un palindromo" if is_valid == True else f"la frase {phrase} no es un palindromo"
)
