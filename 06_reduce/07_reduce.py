# count the total character

from functools import reduce

def count_ch(total, word):
    return total + len(word)

words = ["DS", "DA", "Python", "Java", "Data Science"]

res = reduce(count_ch, words, 0)

print("Total Characters are ::", res)