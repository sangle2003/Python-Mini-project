#Create a Circle class. Use a constructor to initialize radius. Create methods to calculate:
class circle():
    def __init__(self,r):
        
        self.r = r
        
    def area(self):
        result = 3.14 * self.r * self.r
        print("area :: ",result)
    
    def circumference(self):
        result = 2 * 3.14 * self.r
        print("circumference :: ",result)
r = int(input("Enter your radius :: "))        
c1 = circle(r)
c1.area()
c1.circumference()

        
        