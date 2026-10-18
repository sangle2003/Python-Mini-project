from functools import reduce
number = [1,2,3,4,5]
res = reduce(lambda x,y: x+y,number)
print(res)