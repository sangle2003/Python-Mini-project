class Brand:
    def b(self):
        self.brand=input("Enter Brand name : ")
        
class RAM:
    def r(self):
        self.ram=input("Enter RAM size : ")
        
class GamingLaptop(Brand,Ram):
    def g(self):
        self.gaming=input("Enter Gaming Laptop name : ",self.brand)
        
    