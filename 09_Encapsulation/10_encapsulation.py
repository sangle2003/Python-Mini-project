class Product:
    def init_(self,price):
        self ._price=price

    def applydiscount(self, percent):
        self ._price-=(self._ price*percent/100)

    def finalprice(self):
        print(" Total Final Price :: ", self ._ price)

p=Product (10008)
p.applydiscount(int(input("Enter Discount in % :: ")))
p.finalprice()