class Multiplication:
    def __add__(self, num):
        self.num = num
        
    def __mul__(self, other):
        return self.num * other.num
    
m1 = Multiplication(10)
m2 = Multiplication(20)
print(m1*m2)
        