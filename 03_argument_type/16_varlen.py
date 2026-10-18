def demo(*num):
    d=0
    for i in num:
        d+=i
    return d

n = int(input("Enter element :: "))
lst = []

for i in range(n):
    lst.append(int(input("Enter element :: ")))
    
print("sum is ",demo(*lst))