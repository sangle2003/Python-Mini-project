# minimum number from list
from functools import reduce

def minimum(x, y):
    if x < y:
        return x
    else:
        return y

n = int(input("Enter How many elements you want in list :: "))

nums = []

for i in range(n):
    num = int(input("Enter Values :: "))
    nums.append(num)

res = reduce(minimum, nums)

print("Minimum number is ::", res)