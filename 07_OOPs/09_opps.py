class product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
        
p1 =product("Laptop",30000)
print("Name is :: ",p1.name,  "price is :: ",p1.price)

p2 = product("Headphone",40000)
print("Name is :: ",p2.name, "price is :: ",p2.price)