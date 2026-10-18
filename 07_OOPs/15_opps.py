class Vehicle:
    def v(self):
        self.brand=input("Enter Brand name :: ")

class Car(Vehicle):
    def c(self):
        print("Car is :: ", self.brand)

class Bike(Vehicle):
    def b(self):
        print("Bike Is :: ", self.brand)

class SportsBike(Bike):
    def sb(self):
        print("Sport Bike Is :: ", self.brand)
        
c = Car()
c.v()
c.c()

b = Bike()
b.v()
b.b()

sb = SportsBike()
sb.v()
sb.b()
sb.sb()
