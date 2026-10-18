# concatenate the strings
from functools import reduce

def def_words(x, y):
    return x + " " + y

words = ["India", "is", "my", "Country"]

res = reduce(def_words, words)

print(res)