# https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(long_str, short_str):
    counter = 0
    for l in range(0, len(long_str)):
        if short_str ==  long_str[l:l + len(short_str)]:
            counter += 1

    return counter
