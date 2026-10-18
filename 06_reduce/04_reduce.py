from functools import reduce

def minimum(x, y):
    if x < y:
        return x
    else:
        return y

numbers = [10, 40, 60, 77, 99, 10, 0, 1]

res = reduce(minimum, numbers)

print("Minimum number is ::", res)