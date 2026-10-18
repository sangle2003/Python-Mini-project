from abc import ABC,abstractmethod

class Vahicle(ABC):
    @abstractmethod
    def features(self):
        pass
class Car(Vahicle):
    def features(self):
        print("Car has great features with 4 wheels")
        print("Car gives good mileage")
        print("Car price ranges from 3 lakhs to 1 crore")
        print("My Favourite car is :: Audi ")
        
class Bike(Vahicle):
    def features(self):
        
        print("Bike has great features  with 2 wheels ")
        print("Bike has great features with 2 Wheels")
        print("Bike gives good mileage")
        print("Bike price ranges from 70 thousand to 5 lakhs")
        print("My Favourite Bike is :: Jupiter ")
        
class Truck(Vahicle):
    def features(self):
        print("Truck has great features")
        print("Truck gives good mileage")
        print("Truck price ranges from 30 lakhs to 1 crore")
        print("My Favourite Truck is :: Container ")

car=Car()
car.features()
print("\n")

bike=Bike()
bike.features()
print("\n")

truck=Truck()
truck.features()
        
