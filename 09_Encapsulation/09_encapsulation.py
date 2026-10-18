class Ride:
    def init_(self):
        self. fare=0

    def calculate_fare(self,km):
        self. fare=km*12

    def get_fare(self):
        print("Total Fare is :: Rs. ", self ._ fare)
        
r = Ride()
r.calculate_fare(int(input("enter distance in km :: ")))
r.get_fare()