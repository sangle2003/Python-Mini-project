from functools import reduce

n = int(input("Enter how many elements you want in list: "))

nums = []

for i in range(n):
    num = int(input("Enter value: "))
    nums.append(num)

res = reduce(lambda x, y: x * y, nums)

print("Product is:", res)