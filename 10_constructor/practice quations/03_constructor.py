#Create a Car class. Use a constructor to initialize brand, model, and color. Print the car details.
class Car:
    def __init__(self,brand,model,color):
        
        self.brand = brand
        self.model = model
        self.color = color
        
brand = input("Enter your brand :: ")
model = input("Enter your model :: ")
color = input("Enter a color :: ")

c1 = Car(brand,model,color)

print("brand :: ",brand)
print("model :: ",model)
print("color :: ",color)
        