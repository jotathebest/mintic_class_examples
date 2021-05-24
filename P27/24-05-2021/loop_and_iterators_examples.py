# Classical loop iterators

# Lists

my_items = ['a', 'b', 'c']
i = 0
while i < len(my_items):
    print(my_items[i])
    i += 1

for i in range(len(my_items)):
    print(my_items[i])

for item in my_items:
    print(item)

for i, item in enumerate(my_items):
    print(f'{i}: {item}')

# Dictionaries

emails = {
'Bob': 'bob@example.com',
'Alice': 'alice@example.com',
}

for name, email in emails.items():
    print(f'{name} -> {email}')

for value in emails.values():
    print(value)

for key in emails.keys():
    print(key)

# List comprehensions

squares = []
for x in range(10):
    squares.append(x * x)
print(squares)

# values = [expression for item in collection]
squares = [x * x for x in range(10)]
print(squares)

even_squares = [x * x for x in range(10) if x % 2 == 0]

# Beautiful iterators

my_list = []

for x in [20, 40, 60]:
    for y in [2, 4, 6]:
        my_list.append(x * y)

print(my_list)

my_list = [x * y for x in [20, 40, 60] for y in [2, 4, 6]]
print(my_list)
