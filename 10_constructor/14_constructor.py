#Create a Laptop class. Use a constructor to initialize: brand, ram,storage, price
class Laptop:
    def __init__(self,brand,ram,storage,price):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        self.price = price
        
    def display(self):
        print("brand :: ",self.brand)
        print("ram :: ",self.ram)
        print("storage :: ",self.storage)
        print("price :: ",self.price)
        
brand = input("Enter your brand name :: ")
ram =  (input("Enter a ram :: "))
storage = int(input("Enter a how many storage :: "))
price = float(input("Enter a laptop price :: "))

l1 = Laptop(brand,ram,storage,price)
l1.display()
        