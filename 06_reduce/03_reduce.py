from functools import reduce

def maximum(x, y):
    if x > y:
        return x
    else:
        return y

numbers = [10, 40, 60, 77, 99, 10, 0, 1]

res = reduce(maximum, numbers)

print("Maximum number is ::", res)