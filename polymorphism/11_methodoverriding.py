class Ride:
    def calculate_fare(self,discount):
        print("Calculating Fare.....")
        
class BikeRide(Ride):
    def calculate_fare(self,distance):
        print(f"Bike Fare :: Rs. {distance*5}")

class CarRide(Ride):
    def calculate_fare(self,distance):
        print(f"Car Fare :: Rs. {distance*15}")

r1=BikeRide()
r2=CarRide()

r1.calculate_fare(10)
r2.calculate_fare(5)      