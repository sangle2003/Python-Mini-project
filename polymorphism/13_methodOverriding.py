class Order:
    def calculate_total(self, amount):
        return amount

def display(self, amount):
    print(f"Total Amount: <{self.calculate_total(amount)}")

class DineIn(Order):
    def calculate_total(self, amount):
        return amount + 50 # service charge

    def display(self, amount):
        print(f"Dine-In Order + Base: {amount}, Service Charge: <50, Total: {self.calculate_total(amount)}")
        
class Delivery(Order):
    def calculate_total(self, amount):
        return amount + 100 # delivery charge

    def display(self, amount):
        print(f"Delivery Order + Base: <{amount}, Delivery Charge: <100, Total: R{self.calculate_total(amount)}")

# Usage
orders = [DineIn(),TakeAway(), Delivery()]

for order in orders:
    order.display(500)