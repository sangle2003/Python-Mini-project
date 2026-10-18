class Area:
    def Calculate(self,a,b=None):
        if b:
            return a * b
        return a * a
    
ar=Area()
print(ar.Calculate(4)) #square
print(ar.Calculate(4,5)) #rectangle