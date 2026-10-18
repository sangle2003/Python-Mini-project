#Create a Rectangle class. Use a constructor to initialize length and width. Create an area() method to calculate the area.
class Rectangle:
    def __init__(self,length,width):
        
        self.length = length
        self.width = width
        
    def area(self):
        
        return self.length * self.width
    
length = int(input("Enter a rectangle length :: "))
width = int (input("Enter a ectangle width :: "))

r1 = Rectangle(length,width)

print(r1.area())
        