class circle:
    def __init__(self,radius):
        self.radius = radius
        
    def display(self):
        result = 3.14* self.radius * self.radius
        print("radius :: ",result)
        
c1 = circle(4)
c1.display()

        