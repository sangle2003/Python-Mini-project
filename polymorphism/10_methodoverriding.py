class Payment:
    def Pay(self,amount):
        print("Processsing the payment !!!")
        
class CreaditCard(Payment):
    def pay(self,amount):
        print(f"paid Rs. {amount} using Creadit card")

class UPI(Payment):
    def pay(self, amount):
        print(f"Paid Rs. {amount} using UPI")

class Cash(Payment):
    def pay(self, amount):
        print(f"Paid Rs. {amount} using Cash")

p1=CreaditCard()
p2=UPI()
p3=Cash()

p1.pay(20000)
p2.pay(40000)
p3.pay(10000)