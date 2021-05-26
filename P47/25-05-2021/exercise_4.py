# https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(long_str, short_str):
    counter = 0
    for l in range(0, len(long_str)):
        if short_str ==  long_str[l:l + len(short_str)]:
            counter += 1

    return counter

# ABCDCDC
# CDC

# Camilo

def my_finder(main, sub):
    indexes = []
    last_index = None
    for i in range(0, len(main)):
        if main.find(sub, i) != last_index:
            last_index = main.find(sub, i)
            indexes.append(last_index)
            occurrences = len(indexes) - 1
    return occurrences

string = str(input("Write a string: "))
sub_string = str(input("Search for: "))
print(f"The amount of occurrences for '{sub_string}' in '{string}' is: {my_finder(string, sub_string)}") 
