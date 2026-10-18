#product details 
class Product:
    def __init__(self,name,price,quantity):
        self.name = name 
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity
    
name = input("Enter name :: ")
price = float(input("Enter price :: "))
quantity = int (input("Enter quantity :: "))

p = Product(name,price,quantity)
print("Product name is :: ",p.name)
print("Price for each prodrch :: ",p.price)
print("Qusntity of product :: ",p.quantity)
print("Toal cost is :: ",p.total())
