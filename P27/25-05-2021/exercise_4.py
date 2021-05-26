# https://www.hackerrank.com/challenges/find-a-string/problem

# "ABCDFCSD"
# "cdc"
# [indice: >>]

def count_substring(long_str, short_str):
    counter = 0
    for index in range(0, len(long_str)):
        if short_str == long_str[index: index + len(short_str)]:
            counter += 1
    return counter

count_substring(["ABCDEF"], ["CDC"])
