# longest word from list

from functools import reduce

def longest(x, y):
    if len(x) > len(y):
        return x
    else:
        return y

words = ["DS", "DA", "Python", "Java", "Data Science"]

res = reduce(longest, words)

print("Longest word is ::", res)