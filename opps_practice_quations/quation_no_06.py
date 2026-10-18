#area of rectangle 
class Rectangle:
    def __init__(self,length,width):
        self.lenght = length
        self.width = width
        
def Area(self):
    result = self.length * self.width
    print("area :: ",result)
    
r = Rectangle(10,5)
r.Area()
        