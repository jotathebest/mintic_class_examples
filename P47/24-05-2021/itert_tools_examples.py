# Iterating and Making Decisions
"""
Infinite iteratorsInfinite iterators allow you to work with a for loop in a different fashion, 
like if it was a while loop
"""

from itertools import count

for n in count(5, 3):
    if n > 20:
        break
    print(n, end=', ')  # instead of newline, comma and space

"""
The count factory class makes an iterator that just goes on and on counting. It starts from 5 and keeps adding 3 to it. We need to manually break it if we don't want to get stuck in an infinite loop.
"""

# Iterators terminating on the shortest input sequence

"""
very similar to zip()
"""

from itertools import compress
data = range(10)
even_selector = [1, 0] * 10
odd_selector = [0, 1] * 10
even_numbers = list(compress(data, even_selector))
odd_numbers = list(compress(data, odd_selector))
print(odd_selector)
print(list(data))
print(even_numbers)
print(odd_numbers)

# Combinatoric generators

from itertools import permutations
print(list(permutations('ABC')))
