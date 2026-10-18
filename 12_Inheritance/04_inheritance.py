class vehical:
    def get_details(self):
        self.brand = input("Enter Brand Name :: ")
        
class Car(vehical):
    def car_details(self):
        self.name = input("Enter Car Name :: ")
        self.price = int(input("Enter your Price :: "))
        print(self.brand," brand car ",self.name," cost for ",self.price)
        
c1 = Car()
c1.get_details()
c1.car_details()