#Create a Mobile class. Use a constructor to initialize brand, model, and price. Create an object and display all details.
class Mobile:
    def __init__(self,brand,model,color):
        
        self.brand = brand
        self.model = model 
        self.color = color
        
    def display(self):
        print("brand :: ",self.brand)
        print("model :: ",self.model)
        print("color :: ",self.color)
        
m1 = Mobile("samsung","s24","blue")

print(m1.display())


