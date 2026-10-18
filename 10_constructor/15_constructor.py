#Create a Product class with name, price, and quantity.
#If quantity is greater than 5, give a 10% discount. Calculate and display the final bill.
class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def display(self):
        if self.quantity > 5:
            discount = self.price * 10 / 100
            print("you have a 10% discount :: ",discount)
        else:
            print("Your product is less than 5 you have a no discount !!!")
            
name = input ("Enter your name :: ")
price = float(input("Enter your price :: "))
quantity = int (input("Enter your how many product are bye :: "))
p1 = Product(name,price,quantity)
p1.display()
            
            
        