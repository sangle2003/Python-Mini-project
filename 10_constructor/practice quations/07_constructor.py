#Create a BankAccount class. Use a constructor to initialize account_holder and balance. Create a display() method to show the details.
class Bank:
    def __init__(self,account_holder,balance):
        
        self.account_holder = account_holder
        self.balance = balance
        
    def display(self):
        print("Account holder :: ",self.account_holder)
        print("Balance :: ",self.balance)
        
b1 = Bank("pradip",200000)
print(b1.display())
        