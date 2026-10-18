class Number:
    def __init__(self,val):
        self.val = val
        
    def __add__(self, other):
        return self.val + other.val
    
n1 = Number(5)
n2 = Number(10)
print(n1 + n2)
        