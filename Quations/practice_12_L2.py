#find the smaller number.
def smaller(a,b,c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c
    
print(smaller(10,20,30))
print(smaller(40,50,60))