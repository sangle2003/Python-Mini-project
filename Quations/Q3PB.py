#length argument
#total calculation of all elements
def length(*args):
    total = 0
    for i in args:
        total += i
        
    return total

print(length(10,20,30,40,50))