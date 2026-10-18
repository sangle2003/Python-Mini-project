from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass
    
class UPI(Payment):
    def pay(self,amount):
        print("Paid RS. ",amount,"via UPI")
        
class Cash(Payment):
    def pay(self,amount):
        print("paid RS. ",amount,"via card")
        
class card (Payment):
    def pay(self,amount):
        print("paid RS. ",amount,"via card")
        
amount=int(input("Enter Amount :: "))
u=UPI()
u.pay(amount)

amount=int(input("Enter Amount :: "))
c=Cash()
c. pay(amount)

amount=int(input("Enter Amount :: "))