#Create a Product class. Use a constructor to initialize name, price, and quantity. Create a method to calculate the total price.
class Product:
    def __init__(self,name,price,quantity):
        
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def display(self):
        return self.price * self.quantity
    
name = input("Enter your name :: ")
price = float(input("Enter your price :: "))
quantity = int (input("Enter your product quantity :: "))

p1 = Product(name,price,quantity)
print("name :: ",p1.name)
print("price :: ",p1.price)
print("quantity :: ",p1.quantity)
print("Total price :: ",p1.display())
        