from abc import ABC, abstractmethod

# Abstract Class
class FoodOrder (ABC):

    def _init_(self, order_id, amount):
        self. order_id = order_id
        self. amount = amount

# Concrete Method
    def order_details(self):
        print("Order ID:", self.order_id)
        print("Order Amount:", self. amount)

        
#abstact method 
@abstractmethod
def NormalOrader(self):
    pass

# Single Inheritance
class NormalOrder(FoodOrder):

    def calculate_delivery_charge(self):
        return 40

# Hierarchical Inheritance
class ExpressOrder (FoodOrder):

    def calculate_delivery_charge(self):
        return 80

class FreeDeliveryOrder(FoodOrder):

    def calculate_delivery_charge(self):
        return 0
# Multilevel Inheritance
class RestaurantOrder(NormalOrder):

    def restaurant_details(self):
        print("Order is prepared by restaurant")

class PremiumRestaurantOrder(RestaurantOrder):

    def premium_service(self):
        print("Premium restaurant service activated")
        
#object
normal = NormalOrader(101,500)
normal.order_details()
print("Delivery Charge:", normal.calculate_delivery_charge())

print("----------------------")

express = ExpressOrder(102, 800)
express. order_details()
print("Delivery Charge:", express. calculate_delivery_charge())

print("------------------------------")

free = FreeDeliveryOrder(103, 1000)
free.order_details()
print("Delivery Charge:", free. calculate_delivery_charge())

print("------------------------------")

premium = PremiumRestaurantOrder(104, 1000)
premium. order_details()
print("Delivery Charge:", premium.calculate_delivery_charge())
premium. restaurant_details()
premium.premium_service()