class Car:
    def __init__(self,rental,name,day):
        self.rental = rental
        self.name = name
        self.day = day 
        
    def total(self):
        return self.rental * self.day
    
rental = float(input("Enter a rent :: "))
name = input(("Enter your car name :: "))
day = int(input("Enter your day :: "))

c1 = Car(rental,name,day)
print("reant :: ",c1.rental)
print("Car name :: ",c1.name )
print("day :: ",c1.day)
print("total rant price :: ",c1.total())

c2 = Car(rental,name,day)
print("rent :: ",c2.rental)
print("car name :: ",c2.name )
print("day :: ",c2.day)
print("total rant :: ",c2.total())        